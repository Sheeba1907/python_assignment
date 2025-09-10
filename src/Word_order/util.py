def count_distinct_words(words):
  
    word_count = {}
    order = []

    for word in words:
        if word not in word_count:
            word_count[word] = 1
            order.append(word)
        else:
            word_count[word] += 1

    counts = []
    for word in order:
        counts.append(word_count[word])

    return len(order), counts