import numpy as np
from util import mean_var_std

def main():
    n, m = map(int, input("Enter the value of N and M: ").split())
    matrix = []

    # Explicitly build the matrix (no HOF)
    for _ in range(n):
        row_vals = []
        row_input = input("Enter the integers: ").split()
        for val in row_input:
            row_vals.append(int(val))
        matrix.append(row_vals)

    arr = np.array(matrix)
    mean_axis1, var_axis0, std_all = mean_var_std(arr)

    print(mean_axis1)
    print(var_axis0)
    print(std_all)

if __name__ == "__main__":
    main()