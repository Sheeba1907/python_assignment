def mutate_string(strings, index, letter):
    new_string = ""
    for i in range(len(strings)):
        if i == index:
            new_string += letter
        else:
            new_string += strings[i]
    return new_string