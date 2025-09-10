import numpy as np

def mean_var_std(matrix):
    
    mean_axis1 = np.mean(matrix, axis=1)
    var_axis0 = np.var(matrix, axis=0)
    std_all = np.std(matrix, axis=None)

    return mean_axis1, var_axis0, std_all