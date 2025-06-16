import numpy as np
from scipy.stats import zscore

def compute_spread(series1, series2):
    return series1 - series2

def generate_signals(spread, entry_z=2.0, exit_z=0.5):
    zscores = zscore(spread)
    long = zscores < -entry_z
    short = zscores > entry_z
    exit = np.abs(zscores) < exit_z
    return long, short, exit 
