from cipher import encrypt, decrypt

message = input("Enter plaintext or ciphertext: ")
mode = input("encrypt or decrypt: ")
shift = int(input("Shift value (1-365): "))
filename = input("Enter filename with extension: ")

with open(filename) as f:
    words = [word.lower() for line in f for word in line.split()]

words_no_punct = [
    "".join(char for char in word if char.isalpha())
    for word in words
]

word_dict = {}
for i, word in enumerate(words_no_punct):
    if word:
        word_dict.setdefault(word, []).append(i)

if mode == "encrypt":
    encrypted = encrypt(message, word_dict, shift)
    print("encrypted ciphertext =", encrypted)
    decrypted = decrypt(encrypted, words_no_punct, shift)
    print("decrypted plaintext =", decrypted)

elif mode == "decrypt":
    numbers = list(map(int, message.split()))
    decrypted = decrypt(numbers, words_no_punct, shift)
    print("decrypted plaintext =", decrypted)