import numpy as np
import pandas as pd

def backtest_strategy(spread, long_signals, short_signals, exit_signals):
    position = np.zeros(len(spread))
    returns = np.zeros(len(spread))

    for i in range(1, len(spread)):
        if long_signals[i]:
            position[i] = 1
        elif short_signals[i]:
            position[i] = -1
        elif exit_signals[i]:
            position[i] = 0
        else:
            position[i] = position[i-1]

        returns[i] = position[i-1] * (spread[i] - spread[i-1])

    cumulative = np.cumprod(1 + returns) - 1
    return cumulative, returns 
