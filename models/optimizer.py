import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.base import BaseEstimator
from scipy.stats import uniform
from scipy.stats import zscore

class ThresholdStrategy(BaseEstimator):
    def __init__(self, entry_z=2.0, exit_z=0.5):
        self.entry_z = entry_z
        self.exit_z = exit_z

    def fit(self, X, y=None):
        return self

    def score(self, X, y=None):
        spread = X
        zscores = zscore(spread)
        long = zscores < -self.entry_z
        short = zscores > self.entry_z
        exit = np.abs(zscores) < self.exit_z

        position = np.zeros(len(spread))
        returns = np.zeros(len(spread))

        for i in range(1, len(spread)):
            if long[i]:
                position[i] = 1
            elif short[i]:
                position[i] = -1
            elif exit[i]:
                position[i] = 0
            else:
                position[i] = position[i-1]

            returns[i] = position[i-1] * (spread[i] - spread[i-1])

        cumulative = np.cumprod(1 + returns)[-1]
        return cumulative

def optimize_thresholds(spread):
    param_dist = {
        'entry_z': uniform(1.0, 3.0),
        'exit_z': uniform(0.1, 1.0)
    }

    model = ThresholdStrategy()
    search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=20, scoring='r2', cv=3, random_state=42)
    search.fit(spread.reshape(-1, 1))

    best_params = search.best_params_
    return {
        'entry_z': best_params['entry_z'],
        'exit_z': best_params['exit_z']
    }