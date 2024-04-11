def main():
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input(f"Please enter an option: "))
        if option == 1:
            message_to_encode = input("Please enter your password to encode: ")
            message_to_encode = int(message_to_encode)
            encoded_string = str(encoder(message_to_encode))
            print("Your password has been encoded and stored!") 
        if option == 2:
            decode_pass = decoder(encoded_string)
            print(f"The encoded password is {encoded_string}, and the original password is {decode_pass}.")
        if option == 3:
            break

def encoder(password):
    new_password = 0
    for character in str(password):
        character = int(character) +3
        new_password *= 10
        new_password += character
    return new_password

def decoder(encoded_password):
    new_password = ""
    for char in encoded_password:
        char = int(char) - 3
        new_password += str(char)
    return new_password


if __name__ == '__main__':
    main()