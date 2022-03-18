import webbrowser # https://gchq.github.io/CyberChef/
message = 'InsertYourMessageHere' #encrypted message, manual parse out by .replace()also valid
message = message.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    for key in range(26):
        decrypted_message = ""
        for c in message:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c
        ConstructString = decrypted_message[0:5] + "://" + decrypted_message[5:9] + "." + decrypted_message[9:11] + "/" + decrypted_message[11:]
        print(key, ConstructString)
        if decrypted_message.startswith("https"):
            ConstructString = ConstructString.replace("h","H",-1) ##because I converted to lower
            ConstructString  = ConstructString.replace("k","K") # instead of doing 2x the rounds
            ConstructString = ConstructString.replace("x","X") # yeah this could be neater but a flag is a flag
            print("                  Plaintext found!:       " + ConstructString)
            webbrowser.open(ConstructString) #Open it!!!
decrypt()
