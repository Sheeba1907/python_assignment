from util import stack_cubes

def main():
    t = int(input("Enter the integer T: ").strip())
    for _ in range(t):
        n = int(input("Enter the size of each cube: ").strip())
        blocks_input = input("Enter the elements: ").split()
        blocks = []
        for val in blocks_input:
            blocks.append(int(val))
        result = stack_cubes(blocks)
        print(result)

if __name__ == "__main__":
    main()