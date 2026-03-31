from read_file import read_file
from preprocessing import list_to_string, getSwitch
from encode import encode_message
from decode import decode_text

if __name__ == "__main__":
    # Read File
    data = read_file("data/lost.txt")
    
    # Encode Message
    message = input("What is your message ? ")
    switch = getSwitch()
    encoded_message = encode_message(message, data, switch=switch)
    print("The encoded message is :", encoded_message)

    # Decode Message
    decoded_message = decode_text(encoded_message, data, switch=switch)
    print("The decoded message is :", list_to_string(decoded_message))