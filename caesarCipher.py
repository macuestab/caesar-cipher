alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
    
def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

# The easiest way to break this code is to simply brute force though all of the possible shifts.
# We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can 
# look through all of the outputs and look for the one that in english, and we've decoded our message!
def decoderWithoutOffset(coded_message):
    for i in range(1,26):
        print("offset: " + str(i))
        print("\t " + decoder(coded_message, i) + "\n")


# Run the code
offset_flag = True
answer = True
print("What do you want with your message, encode it or decode it?")
codeOrDecode = input("Type \'encode\' or \'decode\': ").lower()
if codeOrDecode == "encode" or codeOrDecode == "decode":
    if codeOrDecode == "encode":
        message = input("Type your message to be encoded: ").lower()
        while offset_flag:
            try:
                offset = int(input("What offset do you want to give?: "))
                offset_flag = False
            except ValueError as e:
                print("Provide a number!")
                print(e)
        print("Encoding message.....")
        print(coder(message, offset))
    else:
        message = input("Type your message to be decoded: ").lower()
        print("Do you know the offset?")
        
        while answer:
            offset = input("Type \'yes\' or \'no\': ").lower()
            if offset == "yes" or offset == "no":
                answer = False
            else:
                print("Please, choose one option between \'yes\' or \'no\'.")
        if offset == "yes":
            while offset_flag:
                try:
                    offset = int(input("Please, type the offset: "))
                    offset_flag = False
                except ValueError as e:
                    print("Provide a number!")
                    print(e)
            print("Decoding message.....")
            print(decoder(message, offset))
        else:
            print("Breaking the code with 25 different shifts.....")
            decoderWithoutOffset(message)
else:
    raise Exception("Please, choose one option between \'encode\' or \'decode\'.")
