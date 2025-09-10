from datetime import datetime

def time_difference(t1: str, t2: str) -> int:
    
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    diff = abs(int((dt1 - dt2).total_seconds()))
    return diff