#!/usr/bin/env python3
"""fitting.py -- fits a two overlapping Gaussian peaks

Starting Code:
Mike Moran
mmoran0032@gmail.com
2016-06-28
Benjamin Rose
benjamin.rose@me.com
2017-06-20
Chris Seymour
seymour.16@nd.edu
2019-06-18
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import statistics as stat


def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.

    Parameters
    ----------
    x : numpy.array
        The input values for the Gaussian function. Similar to the x values 
        used in a plotting command.

    A : float
        Maximum value of the Gaussian.

    mu : float
        Location (along x-axis) for the center of the Gaussian. Maybe outside 
        the range of `x`.

    sigma : float
        Width of the Gaussian.

    Return
    ------
    numpy.array
        A y-value (in a Gaussian shape) for each `x` given.
    """
    return A * np.exp(-(x - mu)**2/(2 * sigma**2))


def fitter(x, A0, mu0, sigma0, A1, mu1, sigma1):
    """
    Function to fit to the data. Two Gaussians that... 
    """
    global G
    global G1
    G= A0 * np.exp(-(x - mu0)**2/(2 * sigma0**2))
    G1= A1 * np.exp(-(x - mu1)**2/(2 * sigma1**2))
    G_total=G+G1
    return G_total


bins, counts = np.loadtxt('two_peaks.txt', unpack=True)
x=np.linspace(0,30,100)
A=np.max(counts)
mu=stat.mean(x)
sigma=stat.stdev(x)


pars, _ = curve_fit(fitter,bins,counts)

plt.scatter(bins, counts)
plt.plot(x, fitter(x, *pars))
plt.plot(x,G)
plt.plot(x,G1,100)
plt.show()
