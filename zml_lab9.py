def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input(f"Please enter an option: ")
        option = int(option)
        if option == 1:
            message_to_encode = input("Please enter your password to encode: ")
            message_to_encode = int(message_to_encode)
            encoded_string = encoder(message_to_encode)
            print("Your password has been encoded and stored!")
        if option == 3:
            break

def encoder(password):
    new_password = 0
    for character in str(password):
        character = int(character) +3
        new_password *= 10
        new_password += character
    return new_password


if __name__ == '__main__':
    main()