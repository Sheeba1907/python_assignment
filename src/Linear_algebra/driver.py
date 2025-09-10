import numpy as np
from util import determinant

def main():
    n = int(input("Enter the dimension N: ").strip())
    matrix = []

    # Explicitly read matrix rows (no HOFs)
    for _ in range(n):
        row_vals = []
        row_input = input("Enter the elements: ").split()
        for val in row_input:
            row_vals.append(float(val))
        matrix.append(row_vals)

    arr = np.array(matrix)
    det = determinant(arr)
    print(det)

if __name__ == "__main__":
    main()