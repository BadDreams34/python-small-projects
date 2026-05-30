"""Tries to find the encrypted message by brutal force in caesar cipher"""

# you will have caesar cipher string as input validation
# you will generate a key which ranges from 0 to 25 which will be decreased from the encoded message and code will be printed

import string
symbols = string.ascii_uppercase

def main():
    message = input("Enter the message to decrypt: ")
    for key in range(26):
        translated = ""
        for char in message:
            if char in symbols:
                index = symbols.find(char) - key
                translated += symbols[index]
            else:
                translated += char

        print("Key #{}: {}".format(key+1, translated))


if __name__ == "__main__":
    main()