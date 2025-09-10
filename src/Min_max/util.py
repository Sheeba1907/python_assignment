import numpy as np

def minmax(arr):
    
    row_mins = np.min(arr, axis=1)
    return np.max(row_mins)