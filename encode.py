from random import randint
from preprocessing import text_to_list

def word_exists(word, data_structure):
    """
    Takes as parameter a data structure (list, tuple or dict) of words
    Returns True if the word is a key in the structure.
    """
    return word in data_structure

def get_index_word(word, D_words):
    """
    Takes as parameter a dictionnary of words associated with its indexes.
    Returns a random index value of the given word.
    Returns -1 if the word does not exists in the given dictionnary
    """
    if (word_exists(word, D_words)):
        indexes = D_words[word]
        return indexes[randint(0, len(indexes)-1)] # returns a random element of indexes
    else:
        return -1 # word does not exist in D_words
    
def get_index_letter(letter, D_letters):
    """
    Takes as parameter a dictionnary of lowercase letters associated with indexes of words beggining with that letter.
    Returns a random index value of the given dictionnary.
    """
    if (len(D_letters) < 26):
        raise ValueError(f"The dictionnary does not have too much letter. Got {D_letters.keys()}")
    
    indexes = D_letters[letter]
    return indexes[randint(0, len(indexes)-1)] # returns a random element of indexes

def encode_proper_word(word, result, D_letters, D_words):
    """
    Encode a proper word. i.e. letter by letter.
    Returns a list of indexes.
    """
    result.append(get_index_word("the", D_words))
    result.append(get_index_word("the", D_words))
    for letter in word:
        result.append(get_index_letter(letter, D_letters))
    result.append(get_index_word("a", D_words))
    result.append(get_index_word("a", D_words))



def encode_word(word, result, D_words, D_letters):
    """
    Encode a word and appends in result the encoded word.
    """
    i = get_index_word(word, D_words)
    if (i == -1):
        encode_proper_word(word, result, D_letters, D_words)
    else:
        result.append(i)


def encode_text(L, D_words, D_letters):
    """
    Takes as parameter a list of words without punctuation and returns the encoded text.
    """
    result = []
    for word in L:
        encode_word(word, result, D_words, D_letters)
    return result

def encode_message(message, D_words, D_letters):
    """
    Encodes a message as a list of integers.
    """
    parsed_text = text_to_list(message)
    encoded_message = encode_text(parsed_text, D_words, D_letters)
    return encoded_message