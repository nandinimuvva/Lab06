#Nandini Muvva's encoder function
def encode(password):
    encoded_password = ""
    for char in password:
        encoded_password = encoded_password + str((int(char) + 3) % 10)
    return encoded_password

#Aadish Kachhal added the decode function.
def decode(password):
    decoded_password = ""
    for char in password:
        if (int(char)-3) < 0:
            decoded_password += str((int(char)-3)+10)
        else:
            decoded_password += str((int(char)-3))
    return decoded_password

#Nandini Muvva's main function
def main():
    encoded_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = str(encode(password))
            print("Your password has been encoded and stored!")
            print("")

        elif option == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")

        elif option == "3":
            break

if __name__ == '__main__':
    main()
