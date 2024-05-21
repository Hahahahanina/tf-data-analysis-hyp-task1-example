import pandas as pd
import numpy as np


chat_id = 1260358058 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    mean_control = x_success / x_cnt
    mean_test = y_success / y_cnt
    alpha = 0.01 
    test = sps.norm(loc=mean_test).rvs(1000)
    control = sps.norm(loc=mean_control).rvs(1000)
    pvalue = sps.ttest_ind(test, control, alternative='less').pvalue
    return pvalue > alpha
