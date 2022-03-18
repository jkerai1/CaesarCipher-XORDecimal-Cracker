Cipher = "YOUR TEXT GOES HERE"

for decim in range(256):
        print(decim, ":", ''.join([chr(ord(char) ^ decim) for char in Cipher]))
        #ord() -return the integer that represents the character "h"
