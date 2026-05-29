import string


def main():
    while True:
        key = input("Enter a key: ")
        if 0 < int(key) < 26:
            key = int(key)
            break


    message = input("Enter a message: ")
    while True:
        status = input("Do you want to (e)ncrypt or (d)ecrypt?")
        if status == "e" or status == "d":
            break

    if status == "e":
        # shifted string
        shifted_lower = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
        shifted_upper = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

        cipher = str.maketrans(string.ascii_lowercase, shifted_lower)
        cipher.update(str.maketrans(string.ascii_uppercase, shifted_upper))

        print(message)
        print("Encrypted message: {}".format(message.translate(cipher)))

    if status == "d":

        #shifted string
        shifted_lower = string.ascii_lowercase[-key:] + string.ascii_lowercase[:-key]
        shifted_upper = string.ascii_uppercase[-key:] + string.ascii_uppercase[:-key]
        decipher = str.maketrans(string.ascii_lowercase, shifted_lower)
        decipher.update(str.maketrans(string.ascii_uppercase, shifted_upper))

        print(message)
        print("Decrypted message: {}".format(message.translate(decipher)))






if __name__ == "__main__":
    main()








