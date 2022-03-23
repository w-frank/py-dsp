"""@package py-dsp

Utility functions for Digital Signal Processing.

This file can also be imported as a module and contains the following
functions:
    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import numpy as np

def find_3db_cutoff_frequency(array):
    """Finds and returns the index of the cutoff frequency (-3 dB) in an array
    of signal amplitudes. Assumes amplitudes are in dB.

    Parameters
    ----------
    array : array
        An array of amplitudes (in dB), python list or numpy array.

    Returns
    -------
    idx
        The index of amplitude value closest to the cutoff frequency (-3 dB)
    """
    cutoff_amp = array[0] - 3 # dB
    array = np.asarray(array)
    idx = (np.abs(array - cutoff_amp)).argmin()
    return idx