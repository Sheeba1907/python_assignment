from util import time_difference

def main():
    t = int(input("Enter the number of tests: ").strip())  
    for _ in range(t):
        t1 = input("Enter time 1: ").strip()
        t2 = input("Enter time 2: ").strip()
        print(time_difference(t1, t2))

if __name__ == "__main__":
    main()