from util import student_average

def main():
    n = int(input("Enter the  number of students: "))
    students = {}
    
    for i in range(n):
        line = input("Enter the name and marks (name 1 2 3 ): ").split()
        name = line[0]
        score = []
        for i in line[1:]:
            score.append(float(i))
        students[name] = score
    
    r = input("Enter the name for finding average: ").strip()
    marks = students[r]
    total = 0
    for m in marks:
        total = total + m
    average = total / len(marks)
    print(f"{average:.2f}")

if __name__ == '__main__':
    main()
    