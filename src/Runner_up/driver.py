from util import runner_up_score

def main():
    n = int(input("Enter the number of participants: "))
    score = input("Enter the scores separated by space: ").split()

    scores = []
    for i in range(len(score)):
        scores.append(int(score[i]))

    r = runner_up_score(scores)
    print(r)

if __name__ == "__main__":
    main()