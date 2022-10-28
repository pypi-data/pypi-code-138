#usr JiangYu
import time
import numpy as np
import astropy.io.fits as fits
import astropy.wcs as wcs
from astropy.table import Table


from FacetClumps import FacetClumps_2D_Funs
from FacetClumps import FacetClumps_3D_Funs

def Change_pix2word(data_wcs, outcat, ndim):
    """
    将算法检测的结果(像素单位)转换到天空坐标系上去
    :param data_wcs: 头文件得到的wcs
    :param outcat: 算法检测核表
    :return:
    outcat_wcs
    """
    clustPeak, clustSum, clustVolume = np.array([outcat['Peak'], outcat['Sum'], outcat['Volume']])
    clustAngle, clustEdge = np.array([outcat['Angle'], outcat['Edge']])
    size1, size2 = np.array([outcat['Size1'], outcat['Size2']])
    if ndim == 2:
        # 2d result
        peak1, peak2 = data_wcs.all_pix2world(outcat['Peak1'], outcat['Peak2'], 1)
        clump_Peak = np.column_stack([peak1, peak2])
        cen1, cen2 = data_wcs.all_pix2world(outcat['Cen1'], outcat['Cen2'], 1)
        clump_Cen = np.column_stack([cen1, cen2])
        clustSize = np.column_stack([size1, size2])
    elif ndim == 3:
        # 3d result
        peak1, peak2, peak3 = data_wcs.all_pix2world(outcat['Peak1'], outcat['Peak2'], outcat['Peak3'], 1)
        clump_Peak = np.column_stack([peak1, peak2, peak3 / 1000])
        cen1, cen2, cen3 = data_wcs.all_pix2world(outcat['Cen1'], outcat['Cen2'], outcat['Cen3'], 1)
        clump_Cen = np.column_stack([cen1, cen2, cen3 / 1000])
        clustSize = np.column_stack([size1, size2, outcat['Size3']])
    id_clumps = np.arange(1, len(clustPeak) + 1, 1)
    outcat_wcs = np.column_stack((id_clumps, clump_Peak, clump_Cen, clustSize, clustPeak,
                                  clustSum, clustVolume, clustAngle, clustEdge))
    return outcat_wcs

def Table_Interface(did_table, data_wcs, ndim):
    """
    ['ID', 'Peak1', 'Peak2', 'Peak3', 'Cen1', 'Cen2', 'Cen3', 'Size1', 'Size2', 'Size3', 'Peak', 'Sum', 'Volume', 'Angle', 'Edge'] -->3d
    ['ID', 'Peak1', 'Peak2', 'Cen1', 'Cen2',  'Size1', 'Size2', 'Peak', 'Sum', 'Volume', 'Angle', 'Edge']-->2d
    """
    Peak = did_table['peak_value']
    Sum = did_table['clump_sum']
    Volume = did_table['clump_volume']
    Angle = did_table['clump_angle']
    Edge = did_table['clump_edge']
    if ndim == 2:
        Peak1 = list(np.array(did_table['peak_location'])[:, 1] + 1)
        Peak2 = list(np.array(did_table['peak_location'])[:, 0] + 1)
        Cen1 = list(np.array(did_table['clump_center'])[:, 1] + 1)
        Cen2 = list(np.array(did_table['clump_center'])[:, 0] + 1)
        Size1 = list(np.array(did_table['clump_size'])[:, 1])
        Size2 = list(np.array(did_table['clump_size'])[:, 0])
        index_id = np.arange(1, len(Peak1) + 1, 1)
        d_outcat = np.hstack([[index_id, Peak1, Peak2, Cen1, Cen2, Size1, Size2, Peak, Sum, Volume, Angle, Edge]]).T
        columns=['ID', 'Peak1', 'Peak2', 'Cen1', 'Cen2', 'Size1', 'Size2', 'Peak', 'Sum', 'Volume', 'Angle', 'Edge']
        units = [None,'pix','pix','pix','pix','pix','pix','K','K','pix','deg',None]
        dtype = ['int','int','int','float32','float32','float32','float32','float32','float32','int','int8','int8']
        units_wcs = [None,'deg','deg','deg','deg','pix','pix','K','K','pix','deg',None]
        dtype_wcs = ['int','float32','float32','float32','float32','float32','float32','float32','float32','int','int8','int8']
        td_outcat = Table(d_outcat,names = columns,dtype=dtype,units=units)
        td_outcat['Peak'].info.format = '.3f'
        td_outcat['Sum'].info.format = '.3f'
        td_outcat_wcs = Change_pix2word(data_wcs, td_outcat, ndim)
        td_outcat_wcs = Table(td_outcat_wcs,names=columns,dtype=dtype_wcs,units=units_wcs)
        format_keys = [ 'Peak1', 'Peak2', 'Cen1', 'Cen2','Peak','Sum']
        for key in format_keys:
            td_outcat_wcs[key].info.format = '.3f'
    elif ndim == 3:
        Peak1 = list(np.array(did_table['peak_location'])[:, 2] + 1)
        Peak2 = list(np.array(did_table['peak_location'])[:, 1] + 1)
        Peak3 = list(np.array(did_table['peak_location'])[:, 0] + 1)
        Cen1 = list(np.array(did_table['clump_center'])[:, 2] + 1)
        Cen2 = list(np.array(did_table['clump_center'])[:, 1] + 1)
        Cen3 = list(np.array(did_table['clump_center'])[:, 0] + 1)
        Size1 = list(np.array(did_table['clump_size'])[:, 2])
        Size2 = list(np.array(did_table['clump_size'])[:, 1])
        Size3 = list(np.array(did_table['clump_size'])[:, 0])
        index_id = np.arange(1, len(Peak1) + 1, 1)
        d_outcat = np.hstack([[index_id, Peak1, Peak2, Peak3, Cen1, Cen2, Cen3, Size1, Size2, Size3,
                               Peak, Sum, Volume, Angle, Edge]]).T
        columns=['ID', 'Peak1', 'Peak2', 'Peak3', 'Cen1', 'Cen2', 'Cen3', 'Size1', 'Size2', 'Size3',
             'Peak', 'Sum', 'Volume', 'Angle', 'Edge']
        units = [None,'pix','pix','pix','pix','pix','pix','pix','pix','pix','K','K','pix','deg',None]
        dtype = ['int','int','int','int','float32','float32','float32','float32','float32',
                 'float32','float32','float32','int','int8','int8']
        units_wcs = [None,'deg','deg','deg','deg','deg','deg','pix','pix','pix','K','K','pix','deg',None]
        dtype_wcs = ['int','float32','float32','float32','float32','float32','float32',
                     'float32','float32','float32','float32','float32','int','int8','int8']
        td_outcat = Table(d_outcat,names = columns,dtype=dtype,units=units)
        td_outcat['Peak'].info.format = '.3f'
        td_outcat['Sum'].info.format = '.3f'
        td_outcat_wcs = Change_pix2word(data_wcs, td_outcat, ndim)
        td_outcat_wcs = Table(td_outcat_wcs,names=columns,dtype=dtype_wcs,units=units_wcs)
        format_keys = [ 'Peak1', 'Peak2', 'Peak3', 'Cen1', 'Cen2', 'Cen3','Peak','Sum']
        for key in format_keys:
            td_outcat_wcs[key].info.format = '.3f'
    return td_outcat,td_outcat_wcs

def Detect(file_name, parameters, mask_name, outcat_name, outcat_wcs_name):
    start_1 = time.time()
    start_2 = time.ctime()
    RMS = parameters[0]
    Threshold = parameters[1]
    KBins = parameters[2]
    Vmm = parameters[3]
    did_table, td_outcat, td_outcat_wcs = [], [], []
    origin_data = fits.getdata(file_name)
    origin_data = np.squeeze(origin_data)
    origin_data[np.isnan(origin_data)] = -999
    ndim = origin_data.ndim
    if ndim == 2:
        did_table = FacetClumps_2D_Funs.Detect_Facet(RMS, Threshold, KBins, Vmm, origin_data)
    elif ndim == 3:
        did_table = FacetClumps_3D_Funs.Detect_Facet(RMS, Threshold, KBins, Vmm, origin_data)
    else:
        raise Exception('Please check the dimensionality of the data!')
    if len(did_table['peak_value']) != 0:
        np.savez(outcat_name[:-4] + '_FacetClumps_npz', did_ConBased=did_table)
        regions_data = did_table['regions_data']
        fits.writeto(mask_name, regions_data, overwrite=True)
        data_wcs = wcs.WCS(fits.getheader(file_name))
        td_outcat,td_outcat_wcs = Table_Interface(did_table, data_wcs, ndim)
        td_outcat.write(outcat_name,overwrite=True)
        td_outcat_wcs.write(outcat_wcs_name,overwrite=True)
        end_1 = time.time()
        end_2 = time.ctime()
        delta_time = np.around(end_1-start_1,2)
        time_record = np.hstack([[start_2, end_2, delta_time]])
        time_record = Table(time_record, names=['Start', 'End', 'DTime'])
        time_record.write(outcat_name[:-4] + '_FacetClumps_time_record.csv',overwrite=True)
        print('Number:', len(did_table['peak_value']))
        print('Time:', delta_time)
    else:
        print('No clumps!')
    did_tables = {}
    did_tables['outcat_table'] = td_outcat
    did_tables['outcat_wcs_table'] = td_outcat_wcs
    did_tables['mask'] = did_table['regions_data']
    return did_tables






