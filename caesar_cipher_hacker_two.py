"""Caesar Cipher Hacker
A program that hacks caesar cipher with the help of
brute force """

print("Caesar Cipher Hacker")

import string

#Must match with the SYMBOLS WHILE ENCRYPTING
SYMBOLS = string.ascii_uppercase #contains all the symbols which will be encrypted

#The message which is to be decrypted
print("Please enter the message to decrypt")
message = input("> ")

#Try every possible key to find the decrypted message
for key in range(len(SYMBOLS)):
    translated = "" #stores decrypted message
    for char in message: # for every letter in the encrypted message
        if char in SYMBOLS:
            index = SYMBOLS.find(char) #get the index of the key
            index = index - key #decrypt the message
            index = index % 26 # for the values which are less than 0
            translated += SYMBOLS[index]
        else:
            translated += char
    #Display the key being tested along with the decrypted message
    print("Key #{}: {}".format(key+1, translated))






