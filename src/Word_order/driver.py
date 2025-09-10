from util import count_distinct_words

def main():
    n = int(input("Enter the integer N: ").strip())
    words = []
    for _ in range(n):
        words.append(input("Enter the word: ").strip())

    distinct_count, counts = count_distinct_words(words)

    print(distinct_count)
    for val in counts:
        print(val, end=' ')
    print() 

if __name__ == "__main__":
    main()