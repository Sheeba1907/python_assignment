from util import add_happiness

def main():
    n, m = map(int, input("Enter the integers N and M: ").split())

    array = []
    for val in input("Enter integer n(Elements of array): ").split():
        array.append(int(val))

    set_like = set()
    for val in input("Enter elements for set A(like): ").split():
        set_like.add(int(val))

    set_dislike = set()
    for val in input("Enter elements for set B(dislike): ").split():
        set_dislike.add(int(val))

    happiness = add_happiness(array, set_like, set_dislike)
    print(happiness)

if __name__ == "__main__":
    main()