import pandas as pd
import numpy as np
from scipy import stats

chat_id = 253630223 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    stats, pval = stats.ks_2samp(x, y, alternative = 'two-sided')
    return pval >= alpha
