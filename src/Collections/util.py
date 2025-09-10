def calculate_average(n: int, headers: list[str], rows: list[list[str]]) -> float:
   
    headers = [h.strip() for h in headers]

    if "MARKS" not in headers:
        raise ValueError("Input does not contain a MARKS column.")

    marks_index = headers.index("MARKS")

    total_marks = 0
    for row in rows:
        total_marks += int(row[marks_index])

    return total_marks / n