"""@package py-dsp

Utility functions for Digital Signal Processing.

This file can also be imported as a module and contains the following
functions:
    * adc_counts_to_volts - Convert ADC counts to voltages.
    * find_3db_cutoff_frequency - Finds and returns the index of the cutoff
    frequency (-3 dB) in an array of signal amplitudes.
"""

import numpy as np

def adc_counts_to_volts(adc_range, adc_bits, adc_counts):
    """Convert ADC counts to voltage.

    Parameters
    ----------
    adc_range : float
        Voltage range of the ADC.

    adc_bits : integer
        Bit depth of the ADC.

    adc_counts : integer array
        ADC value(s) in counts.

    Returns
    -------
    volts : float array
        Array of voltage values.
    """
    volts = [adc_range*(count/((2**adc_bits)-1)) for count in adc_counts]
    return volts

def find_3db_cutoff_frequency(array):
    """Finds and returns the index of the cutoff frequency (-3 dB) in an array
    of signal amplitudes. Assumes amplitudes are in dB.

    Parameters
    ----------
    array : array
        An array of amplitudes (in dB), python list or numpy array.

    Returns
    -------
    idx : integer
        The index of amplitude value closest to the cutoff frequency (-3 dB)
    """
    cutoff_amp = array[0] - 3 # dB
    array = np.asarray(array)
    idx = (np.abs(array - cutoff_amp)).argmin()
    return idx