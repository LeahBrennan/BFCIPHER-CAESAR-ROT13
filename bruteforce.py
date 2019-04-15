message = input("What is your message? ")

key = int(input("What would you like your offset to be (3 or 13)? "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alphabet = "abcdefghijklmnopqrstuvwyz"
count = 0
while count == 0:
    mode = str(input("Would you like to encrypt or decrypt? "))
    if mode == "encrypt" or mode == "Encrypt" or mode == "E" or mode == "e":
        count = count + 1
    elif mode == "decrypt" or mode == "Decrypt" or mode == "D" or mode == "d":
        count = count + 1
    else:
        print("You need to enter in a valid answer. Please try again. ")



translated_message = ""

for character in message:
    if character in alphabet:
       number = alphabet.find(character)
       if mode == "encrypt" or mode == "Encrypt" or mode == "E" or mode == "e":
           number = number + key
       elif mode == "decrypt" or mode == "Decrypt" or mode == "D" or mode == "d":
           number = number - key



       if number >= len(alphabet):
            number = number - len(alphabet)
       elif number < 0:
            number = number + len(alphabet)


       translated_message = translated_message + alphabet[number]

    else:
         translated_message = translated_message + character

print(translated_message)




#Source: https://stackoverflow.com/questions/36150132/caesar-cipher-with-a-keyword-python
