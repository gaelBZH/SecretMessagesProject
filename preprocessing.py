def text_to_list(txt):
    """
    Takes in parameter a string and return a list of words without punctuation
    """
    words = txt.lower().split()
    words_no_punct = ["".join(char for char in word if char.isalpha()) for word in words]
    return [w for w in words_no_punct if len(w)>0]

def list_to_word(L):
    """
    Takes in parameter a List of words and returns a string cotaining only the first letters.
    """
    result = ""
    for word in L:
        if (word != ""):
            result += word[0]
    return result

def list_to_string(L):
    result = ""
    for i in range(len(L)-1):
        result += L[i] + " "
    return result + L[-1]