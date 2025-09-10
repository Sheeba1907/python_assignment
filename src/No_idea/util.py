def add_happiness(array, set_like, set_dislike):
 
    happiness = 0
    for val in array:
        if val in set_like:
            happiness += 1
        elif val in set_dislike:
            happiness -= 1
    return happiness