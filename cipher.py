import random

def encrypt(message, word_dict, shift):
    result = []

    for word in message.lower().split():
        if word in word_dict:
            index = random.choice(word_dict[word])
            result.append(index + shift)
        else:
            print(f"Word '{word}' not in dictionary.")

    return result


def decrypt(numbers, words_list, shift):
    result = []

    for num in numbers:
        index = num - shift
        if 0 <= index < len(words_list):
            result.append(words_list[index])
        else:
            result.append("?")

    return " ".join(result)