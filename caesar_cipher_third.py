"""A caesar cipher program in which a number is encrypted with
   a given key as well as it is decrypted with the given key."""

try:
    import pyperclip
except ImportError:
    pass # Do nothing if pyperclip isn't installed

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    #ask for mode
    while True:
        mode = input("Do you want to encrypt or decrypt?\n> ")
        if mode.lower() in ["decrypt","encrypt"]:
            break
        print("Please specify if you want to encrypt or decrypt: ")

    #ask for the message
    print("Enter the message to {}".format(mode))
    response = input("> ")

    #ask for the key
    print("Please enter the key to {}".format(mode))
    while True:
        max_key = len(symbols) - 1  # len(symbols) - 1 is the highest index
        key = input("> ")
        if not key.isdecimal():
            continue
        if 0 <= int(key) < max_key:
            key = int(key)
            break
        print("Please enter a valid key")

    #only works on uppercase letters
    response = response.upper()

    #stores the decrypted/encrypted form of the message
    translated = ""

    #encrypt/decrypt each symbol in response
    for char in response:
        if char in symbols:
            index = symbols.index(char)
            if mode == "encrypt":
                index = (index + key) % len(symbols)
            if mode == "decrypt":
                index = (index - key) % len(symbols)

            translated += symbols[index]
        else:
            translated += char


    print(translated)
    return translated

if __name__ == "__main__":
    translated = main()
    try:
        pyperclip.copy(translated)
        print("The message has been copied to your clipboard")
    except:
        pass #Do nothing if pyperclip isn't installed
