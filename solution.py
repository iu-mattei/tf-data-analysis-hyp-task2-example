import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 253630223 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    return anderson_ksamp([x, y]).pvalue < alpha
