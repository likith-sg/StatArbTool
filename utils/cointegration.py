from statsmodels.tsa.stattools import coint

def check_cointegration(series1, series2):
    score, pval, _ = coint(series1, series2)
    return pval < 0.05, pval 
