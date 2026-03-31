def read_file(filename):
    """
    Takes as parameter a file path and returns a list of words without punctuation.
    """
    words_no_punct = []

    with open(filename) as f:
        for line in f:
            for word in line.lower().split():
                clean_word = "".join(char for char in word if char.isalpha())
                if clean_word != "":
                    words_no_punct.append(clean_word)
    return words_no_punct
    
def create_histograms(words):
    """
    Takes as parameter a list of words (without punctuation)
    Returns a dictionnary D_words where :
    - keys are the words
    - values are list of indexes where the words are located
    and another dictionnary D_letters where :
    - keys are the letters lowercase letters [a-z]
    - values are list of indexes where the words begginings with that letter are located
    """
    D_words = {}
    D_letters = {}
    for i in range(len(words)):
        word = words[i].lower()
        letter = word[0]

        # First Dictionnary
        if word in D_words:
            D_words[word].append(i)
        else:
            D_words[word] = [i]

        # Second Dictionnary
        if letter in D_letters:
            D_letters[letter].append(i)
        else:
            D_letters[letter] = [i]
    return D_words, D_letters