import math

def probability_select(arr, k):

    n = len(arr)
    count_a = 0
    for val in arr:
        if val == 'a':
            count_a += 1

    if k > n:
        return 0.0

    if count_a == 0:
        return 0.0
    if count_a == n:
        return 1.0

    total_comb = math.comb(n, k)
    comb_without_a = math.comb(n - count_a, k) if k <= n - count_a else 0
    prob_none = comb_without_a / total_comb

    prob_at_least_one = 1 - prob_none
    return round(prob_at_least_one, 4)