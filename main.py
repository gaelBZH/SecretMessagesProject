from read_file import read_file, create_histograms 
from preprocessing import text_to_list
from encode import encode_text
from decode import decode_text

# Read File
data = read_file("data/lost.txt")
D_words, D_letters = create_histograms(data)

# Encode Message
message = input("What is your message ? ")
parsed_text = text_to_list(message)
encoded_message = encode_text(parsed_text, D_words, D_letters)
print("The encoded message is :", encoded_message)

# Decode Message
decoded_message = decode_text(encoded_message, data)
print("The decoded message is :", decoded_message)