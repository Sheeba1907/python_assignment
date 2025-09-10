from util import calendar_module

def main():
    raw = input("Enter the date in MM DD YYYY format: ").split()
    month = int(raw[0])
    day = int(raw[1])
    year = int(raw[2])

    result = calendar_module(month, day, year)

    print(result)

if __name__ == "__main__":
    main()