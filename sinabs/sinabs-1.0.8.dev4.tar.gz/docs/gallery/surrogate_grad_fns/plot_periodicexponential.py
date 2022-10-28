"""
===================
PeriodicExponential
===================
:class:`~sinabs.activation.PeriodicExponential` surrogate gradient.
"""

import torch
import sinabs.activation as sina
import matplotlib.pyplot as plt

x = torch.linspace(-2, 4, 500)
plt.plot(
    x,
    sina.PeriodicExponential()(v_mem=x, spike_threshold=1.0),
    label="PeriodicExponential",
)
plt.xlabel("Neuron membrane potential")
plt.ylabel("Derivative")
plt.legend()
