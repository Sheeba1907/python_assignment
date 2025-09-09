def runner_up_score(scores):
    unique = list(set(scores))
    unique.sort(reverse = True)
    if len(unique)<2:
        return None
    return unique[1]