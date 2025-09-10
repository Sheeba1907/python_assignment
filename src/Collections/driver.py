from util import calculate_average

def main():
    n = int(input("Enter the number of students: ").strip()) 

    headers = input("Enter the name of the columns: ").strip().split()

    rows = []
    for _ in range(n):
        row = input("Enter the ID, Marks, Name and Class: ").strip().split()
        rows.append(row)

    avg = calculate_average(n, headers, rows)
    print(f"{avg:.2f}")

if __name__ == "__main__":
    main()