from util import probability_select

def main():
    n = int(input("Enter integer N: ").strip())
    arr = input("Enter the elements in lowercase: ").strip().split()
    k = int(input("Enter the index K: ").strip())

    prob = probability_select(arr, k)
    print(prob)

if __name__ == "__main__":
    main()