from util import text_aligning

def main():
    thickness = int(input("Enter the thickness value: ").strip())

    logo_lines = text_aligning(thickness)

    for line in logo_lines:
        print(line)

if __name__ == "__main__":
    main()