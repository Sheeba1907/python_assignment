def merge_tools(s, k):
    result = []
    for i in range(0, len(s), k):
        substring = s[i : i + k]
        seen = ''
        for i in substring:
            if i not in seen:
                seen += i
        result.append(seen)   
    return result