import numpy as np
from util import minmax

def main():
    n, m = map(int, input("Enter the value of N and M: ").split())

    # Explicitly build array (no HOFs)
    matrix = []
    for _ in range(n):
        row = input("Enter the integers: ").split()
        row_vals = []
        for val in row:
            row_vals.append(int(val))
        matrix.append(row_vals)

    arr = np.array(matrix)
    result = minmax(arr)

    print(result)

if __name__ == "__main__":
    main()