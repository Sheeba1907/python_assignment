from util import merge_tools

def main():
    s = input("Enter a string containing duplicates: ")
    k = int(input("Enter the length: "))

    result = merge_tools(s, k)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()