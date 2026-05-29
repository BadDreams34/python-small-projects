import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def main():
    while True:
        encryption_stat = input("Do you want to (e)ncrypt or (d)ecrypt?")
        if encryption_stat == "e" or encryption_stat == "d":
            break

    while True:
        key = input("Enter a key (enter 0 to exit): ")
        if key == "0":
            print("Goodbye!")
            sys.exit()
        elif key.isdecimal() and int(key) < 26:
            break

    if encryption_stat == "e":
        # take the encryption message
        text = input("Enter text to be encrypted: ")
        print("Decrypted text: {}".format(text))


        #shift the text by key
        decrypted_text = ""
        for letter in text:
            if letter.lower() in alphabet:
                shifted_index = (alphabet.index(letter.lower()) + int(key)) % 26
                if letter.islower():
                    decrypted_text += alphabet[shifted_index]
                else:
                    decrypted_text += alphabet[shifted_index].upper()
            else:
                decrypted_text += letter

        print("Encrypted text: {}".format(decrypted_text))

    if encryption_stat == "d":
        text = input("Enter text to be decrypted: ")
        print("Encrypted text: {}".format(text))
        encrypted_text = ""
        for letter in text:
            if letter.lower() in alphabet:
                shifted_index = (alphabet.index(letter.lower()) - int(key)) % 26
                if letter.islower():
                    encrypted_text += alphabet[shifted_index]
                else:
                    encrypted_text += alphabet[shifted_index].upper()
            else:
                encrypted_text += letter
        print("Decrypted text: {}".format(encrypted_text))

if __name__ == "__main__":
    main()