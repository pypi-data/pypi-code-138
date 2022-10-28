from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import numpy as np

import discretize
from SimPEG import maps, mkvc, utils, Data
from ....utils import meshTensor
from ..receivers import Point1DImpedance, Point3DImpedance, Point3DTipper, Point3DComplexResistivity
#     rxList.append(ns.Rx.Point3DComplexResistivity(locations=None,locations_e=rx_loc, locations_h=rx_loc, orientation=rx_orientation, component='phase'))
from ..survey import Survey
from ..sources import Planewave_xy_1Dprimary, Planewave_xy_1DhomotD
from ..simulation import Simulation3DPrimarySecondary
from .data_utils import appResPhs

np.random.seed(1100)
# Define the tolerances
TOLr = 5e-2
TOLp = 5e-2


def getAppResPhs(NSEMdata, survey):
    NSEMdata = Data(dobs=NSEMdata, survey=survey)
    # Make impedance
    zList = []
    for src in survey.source_list:
        zc = [src.freq]
        for rx in src.receiver_list:
            if "imag" in rx.component:
                m = 1j
            else:
                m = 1
            zc.append(m * NSEMdata[src, rx])
        zList.append(zc)
    return [
        appResPhs(zList[i][0], np.sum(zList[i][1:3])) for i in np.arange(len(zList))
    ]


def setup1DSurvey(sigmaHalf, tD=False, structure=False):

    # Frequency
    nFreq = 33
    freqs = np.logspace(3, -3, nFreq)
    # Make the mesh
    ct = 5
    air = meshTensor([(ct, 25, 1.3)])
    # coreT0 = meshTensor([(ct,15,1.2)])
    # coreT1 = np.kron(meshTensor([(coreT0[-1],15,1.3)]),np.ones((7,)))
    core = np.concatenate(
        (np.kron(meshTensor([(ct, 15, -1.2)]), np.ones((10,))), meshTensor([(ct, 20)]))
    )
    bot = meshTensor([(core[0], 20, -1.3)])
    x0 = -np.array([np.sum(np.concatenate((core, bot)))])
    m1d = discretize.TensorMesh([np.concatenate((bot, core, air))], x0=x0)
    # Make the model
    sigma = np.zeros(m1d.nC) + sigmaHalf
    sigma[m1d.gridCC > 0] = 1e-8
    sigmaBack = sigma.copy()
    # Add structure
    if structure:
        shallow = (m1d.gridCC < -200) * (m1d.gridCC > -600)
        deep = (m1d.gridCC < -3000) * (m1d.gridCC > -5000)
        sigma[shallow] = 1
        sigma[deep] = 0.1

    rxList = []
    for rxType in ["z1d", "z1d"]:
        rxList.append(Point1DImpedance(mkvc(np.array([0.0]), 2).T, "real"))
        rxList.append(Point1DImpedance(mkvc(np.array([0.0]), 2).T, "imag"))
    # Source list
    srcList = []
    if tD:
        for freq in freqs:
            srcList.append(Planewave_xy_1DhomotD(rxList, freq))
    else:
        for freq in freqs:
            srcList.append(Planewave_xy_1Dprimary(rxList, freq))

    survey = Survey(srcList)
    return (survey, sigma, sigmaBack, m1d)


def setupSimpegNSEM_PrimarySecondary(inputSetup, freqs, comp="Imp", singleFreq=False):
    rx_x, rx_y = np.meshgrid(np.linspace(-5000, 5000, 5), np.linspace(-5000, 5000, 5))

    rx_loc = np.hstack((mkvc(rx_x, 2), mkvc(rx_y, 2), np.zeros((np.prod(rx_x.shape), 1))))

    csx = 2000.
    csz = 2000.

    mesh = discretize.TensorMesh([
        [(csx, 1, -3), (csx, 6), (csx, 1, 3)],
        [(csx, 1, -3), (csx, 6), (csx, 1, 3)],
        [(csz, 1, -3), (csz, 6), (csz, 1, 3)]
    ], x0="CCC")

    active = mesh.gridCC[:, 2] < 50
    sig = np.ones(mesh.nC) * 0.01
    sig[~active] = 1e-8
    model_true = np.log(sig)

    print(model_true.shape, mesh.nE * 2, active.sum())

    rx_loc[:, 2] = -50

    rxList = []
    if comp == "All":
        rx_type_list = ["xx", "xy", "yx", "yy", "zx", "zy"]
    elif comp == "Imp":
        rx_type_list = ["xx", "xy", "yx", "yy"]
    elif comp == "Tip":
        rx_type_list = ["zx", "zy"]
    elif comp == "Res":
        rx_type_list = ["yx", "yy"]
    else:
        rx_type_list = [comp]

    for rx_type in rx_type_list:
        if rx_type in ["xx", "xy", "yx", "yy"]:
            if comp == "Res":
                rxList.append(Point3DComplexResistivity(locations=rx_loc, orientation=rx_type, component='apparent_resistivity'))
                rxList.append(Point3DComplexResistivity(locations=rx_loc, orientation=rx_type, component='phase'))
            else:
                rxList.append(Point3DImpedance(rx_loc, rx_type, "real"))
                rxList.append(Point3DImpedance(rx_loc, rx_type, "imag"))
        if rx_type in ["zx", "zy"]:
            rxList.append(Point3DTipper(rx_loc, rx_type, "real"))
            rxList.append(Point3DTipper(rx_loc, rx_type, "imag"))

    srcList = []
    if singleFreq:
        # srcList.append(Planewave_xy_1Dprimary(rxList, singleFreq, sigma_primary=sigBG))
        srcList.append(Planewave_xy_1Dprimary(rxList, singleFreq))
    else:
        for freq in freqs:
            # srcList.append(Planewave_xy_1Dprimary(rxList, freq, sigma_primary=sigBG))
            srcList.append(Planewave_xy_1Dprimary(rxList, freq))

    # Survey MT
    survey_ns = Survey(srcList)
    survey_ns.m_true = model_true

    # write out the true model
    # discretize.TensorMesh.writeUBC(mesh,'Mesh-pre.msh', models={'Sigma-pre.dat': np.exp(model_true)})
    # create background conductivity model
    sigma_back = 1e-2
    sigBG = np.zeros(mesh.nC)*sigma_back
    sigBG[~active] = 1e-8

    # Set the mapping
    actMap = maps.InjectActiveCells(
        mesh=mesh, indActive=active, valInactive=np.log(1e-8))
    mapping = maps.ExpMap(mesh) * actMap
    # print(survey_ns.source_list)
    # # Setup the problem object
    sim = Simulation3DPrimarySecondary(
        mesh, survey=survey_ns, sigmaPrimary=sigBG,
        sigmaMap=mapping
    )

    # create the test model
    block = [
        csx*np.r_[-3, 3],
        csx*np.r_[-3, 3],
        csz*np.r_[-6, -1]
    ]

    block_sigma = 3e-1

    block_inds = (
        (mesh.gridCC[:, 0] >= block[0].min()) & (mesh.gridCC[:, 0] <= block[0].max()) & 
        (mesh.gridCC[:, 1] >= block[1].min()) & (mesh.gridCC[:, 1] <= block[1].max()) &
        (mesh.gridCC[:, 2] >= block[2].min()) & (mesh.gridCC[:, 2] <= block[2].max())
    )

    m = model_true.copy()
    m[block_inds] = np.log(block_sigma)
    m = m[active]

    # f = sim.fields(m)

    # TOLr = 5e-2
    # TOL = 1e-4
    # FLR = 1e-20

    # w = np.random.rand(len(m),)
    # v = np.random.rand(sim.survey.nD,)
    # vJw = v.ravel().dot(sim.Jvec(m, w, f))
    # wJtv = w.ravel().dot(sim.Jtvec(m, v, f))

    return (m, sim)


def setupSimpegNSEM_ePrimSec(inputSetup, comp="Imp", singleFreq=False, expMap=True):

    M, freqs, sig, sigBG, rx_loc = inputSetup
    # Make a receiver list
    rxList = []
    if comp == "All":
        rx_type_list = ["xx", "xy", "yx", "yy", "zx", "zy"]
    elif comp == "Imp":
        rx_type_list = ["xx", "xy", "yx", "yy"]
    elif comp == "Tip":
        rx_type_list = ["zx", "zy"]
    elif comp == "Res":
        rx_type_list = ["yx", "yy"]
    else:
        rx_type_list = [comp]

    for rx_type in rx_type_list:
        if rx_type in ["xx", "xy", "yx", "yy"]:
            if comp == "Res":
                rxList.append(Point3DComplexResistivity(locations=rx_loc, orientation=rx_type, component='apparent_resistivity'))
                rxList.append(Point3DComplexResistivity(locations=rx_loc, orientation=rx_type, component='phase'))
            else:
                rxList.append(Point3DImpedance(rx_loc, rx_type, "real"))
                rxList.append(Point3DImpedance(rx_loc, rx_type, "imag"))
        if rx_type in ["zx", "zy"]:
            rxList.append(Point3DTipper(rx_loc, rx_type, "real"))
            rxList.append(Point3DTipper(rx_loc, rx_type, "imag"))

    # Source list
    srcList = []

    if singleFreq:
        # srcList.append(Planewave_xy_1Dprimary(rxList, singleFreq, sigma_primary=sigBG))
        srcList.append(Planewave_xy_1Dprimary(rxList, singleFreq))
    else:
        for freq in freqs:
            # srcList.append(Planewave_xy_1Dprimary(rxList, freq, sigma_primary=sigBG))
            srcList.append(Planewave_xy_1Dprimary(rxList, freq))
    # Survey NSEM
    survey = Survey(srcList)

    # Setup the problem object
    sigma1d = M.r(sigBG, "CC", "CC", "M")[0, 0, :]

    if expMap:
        problem = Simulation3DPrimarySecondary(M,
            survey=survey,
            sigmaPrimary=np.log(sigBG),
            sigmaMap=maps.ExpMap(M)
        )
        problem.model = np.log(sig)
    else:
        problem = Simulation3DPrimarySecondary(M,
            survey=survey,
            sigmaPrimary=sigBG,
            sigmaMap=maps.IdentityMap(M)
        )
        problem.model = sig
    problem.verbose = False
    try:
        from pymatsolver import Pardiso

        problem.solver = Pardiso
    except:
        pass

    return (survey, problem)


def getInputs():
    """
    Function that returns Mesh, freqs, rx_loc, elev.
    """
    # Make a mesh
    M = discretize.TensorMesh(
        [
            [(200, 6, -1.5), (200.0, 4), (200, 6, 1.5)],
            [(200, 6, -1.5), (200.0, 4), (200, 6, 1.5)],
            [(200, 8, -1.5), (200.0, 8), (200, 8, 1.5)],
        ],
        x0=["C", "C", "C"],
    )  # Setup the model
    # Set the frequencies
    freqs = np.logspace(1, -3, 5)
    elev = 0

    # Setup the the survey object
    # Receiver locations
    rx_x, rx_y = np.meshgrid(np.arange(-350, 350, 200), np.arange(-350, 350, 200))
    rx_loc = np.hstack(
        (mkvc(rx_x, 2), mkvc(rx_y, 2), elev + np.zeros((np.prod(rx_x.shape), 1)))
    )

    return M, freqs, rx_loc, elev


def random(conds):
    """ Returns a random model based on the inputs"""
    M, freqs, rx_loc, elev = getInputs()

    # Backround
    sigBG = np.ones(M.nC) * conds
    # Add randomness to the model (10% of the value).
    sig = np.exp(np.log(sigBG) + np.random.randn(M.nC) * (conds) * 1e-1)

    return (M, freqs, sig, sigBG, rx_loc)


def halfSpace(conds):
    """ Returns a halfspace model based on the inputs"""
    M, freqs, rx_loc, elev = getInputs()

    # Model
    ccM = M.gridCC
    # conds = [1e-2]
    groundInd = ccM[:, 2] < elev
    sig = np.zeros(M.nC) + 1e-8
    sig[groundInd] = conds
    # Set the background, not the same as the model
    sigBG = np.zeros(M.nC) + 1e-8
    sigBG[groundInd] = conds

    return (M, freqs, sig, sigBG, rx_loc)


def blockInhalfSpace(conds):
    """ Returns a block in a halfspace model based on the inputs"""
    M, freqs, rx_loc, elev = getInputs()

    # Model
    ccM = M.gridCC
    # conds = [1e-2]
    groundInd = ccM[:, 2] < elev
    sig = utils.model_builder.defineBlock(
        M.gridCC, np.array([-1000, -1000, -1500]), np.array([1000, 1000, -1000]), conds
    )
    sig[~groundInd] = 1e-8
    # Set the background, not the same as the model
    sigBG = np.zeros(M.nC) + 1e-8
    sigBG[groundInd] = conds[1]

    return (M, freqs, sig, sigBG, rx_loc)


def twoLayer(conds):
    """ Returns a 2 layer model based on the conductivity values given"""
    M, freqs, rx_loc, elev = getInputs()

    # Model
    ccM = M.gridCC
    groundInd = ccM[:, 2] < elev
    botInd = ccM[:, 2] < -3000
    sig = np.zeros(M.nC) + 1e-8
    sig[groundInd] = conds[1]
    sig[botInd] = conds[0]
    # Set the background, not the same as the model
    sigBG = np.zeros(M.nC) + 1e-8
    sigBG[groundInd] = conds[1]

    return (M, freqs, sig, sigBG, rx_loc)
