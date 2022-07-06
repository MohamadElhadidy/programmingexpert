def get_n_longest_unique_words(words, n):
    dic = {}
    for word in words:
        if words.count(word) == 1:
            dic[word] = len(word)
    return sorted(dic,reverse= True, key=dic.get)[:n]