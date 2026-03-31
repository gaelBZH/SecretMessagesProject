from read_file import read_file, create_histograms
from preprocessing import list_to_string 
from encode import encode_message
from decode import decode_text

if __name__ == "__main__":
    # Read File
    data = read_file("data/lost.txt")
    D_words, D_letters = create_histograms(data)

    # Encode Message
    message = input("What is your message ? ")
    encoded_message = encode_message(message, D_words, D_letters)
    print("The encoded message is :", encoded_message)

    # Decode Message
    decoded_message = decode_text(encoded_message, data)
    print("The decoded message is :", list_to_string(decoded_message))