def text_aligning(thickness: int, char: str = "H") -> list[str]:
    
    if thickness < 1 or thickness % 2 == 0:
        raise ValueError("Thickness must be a positive odd number.")

    lines = []

    for i in range(thickness):
        line = (char * i).rjust(thickness - 1) + char + (char * i).ljust(thickness - 1)
        lines.append(line)

    for i in range(thickness + 1):
        line = (char * thickness).center(thickness * 2) + (char * thickness).center(thickness * 6)
        lines.append(line)

    for i in range((thickness + 1) // 2):
        line = (char * thickness * 5).center(thickness * 6)
        lines.append(line)

    for i in range(thickness + 1):
        line = (char * thickness).center(thickness * 2) + (char * thickness).center(thickness * 6)
        lines.append(line)

    for i in range(thickness):
        line = (
            (char * (thickness - i - 1)).rjust(thickness)
            + char
            + (char * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
        lines.append(line)

    return lines