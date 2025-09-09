from util import mutate_string

def main():
    strings = input("Enter the string: ")
    line = input("Enter index and character (e.g., '5 k'): ").split()
    index = int(line[0])
    letter = line[1]

    result = mutate_string(strings, index, letter)
    print(result)

if __name__ == "__main__":
    main()