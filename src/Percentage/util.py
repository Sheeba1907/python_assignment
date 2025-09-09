def student_average(name, *marks):
    total = sum(marks)
    avg = total / len(marks)
    return round(avg, 2)