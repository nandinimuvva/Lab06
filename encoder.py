#Nandini Muvva's encoder function
def encode(password):
    encoded_password = ""
    for char in password:
        encoded_password = encoded_password + str((int(char) + 3) % 10)
    return encoded_password


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
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        elif option == "2":
            pass

        elif option == "3":
            print("Exiting program.")
            break

if __name__ == '__main__':
    main()
