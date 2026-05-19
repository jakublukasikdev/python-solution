
def shared_words(a, b):

    return sorted(list(set(a) & set(b)), key=len)

