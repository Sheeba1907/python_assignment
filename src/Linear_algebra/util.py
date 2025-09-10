import numpy as np

def determinant(matrix):
    
    det = np.linalg.det(matrix)
    return round(det, 2)