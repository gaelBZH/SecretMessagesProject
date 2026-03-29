from preprocessing import list_to_word

def decode_word(i, data):
    return data[i]

def decode_text(L, data):
    result = []
    temp = [] # for letters
    letter_mode = False # False -> Decoding words, True -> Decoding letters
    for index in L:
        if letter_mode:
            temp.append(decode_word(index, data))
        else:
            result.append(decode_word(index, data))

        if (len(result) >= 2 and result[-1] == "the" and result[-2] == "the"):
            result.pop()
            result.pop()
            letter_mode = True
        if (len(temp) >= 2 and temp[-1] == "a" and temp[-2] == "a"):
            letter_mode = False
            temp.pop()
            temp.pop()
            txt = list_to_word(temp)
            if (txt != ""):
                result.append(txt)
    return result