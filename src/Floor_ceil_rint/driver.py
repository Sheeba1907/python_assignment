import numpy as np
from util import floor_ceil_rint

def main():
    raw = input("Enter the  input containing the space separated elements: ").split()

    numbers = []
    for val in raw:
        numbers.append(float(val))

    arr = np.array(numbers)

    floor, ceil, rint = floor_ceil_rint(arr)

    print(floor)
    print(ceil)
    print(rint)

if __name__ == "__main__":
    main()