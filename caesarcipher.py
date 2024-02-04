alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shiftamount): 
  mes=""
  for i in message:
    if i in alphabet:
      position=alphabet.index(i)
      newposition=(position+shiftamount)%len(alphabet)
      newletter=alphabet[newposition]
      mes+=newletter
    else:
       mes+=i
  print(f"The encoded text is {mes}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(message, shiftamount):
  mes=""
  for i in message:
    if i in alphabet:
      position=alphabet.index(i)
      newposition=(position-shiftamount)%len(alphabet)
      newletter=alphabet[newposition]
      mes+=newletter
    else:
      mes+=i
  print(f"The decoded text is {mes}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

bool=True
while bool:
  if direction=="encode":
    bool=False
    encrypt(message=text, shiftamount=shift)
  elif direction=="decode":
    bool=False
    decrypt(message=text, shiftamount=shift)
  else:
    print("Wrong input try again")
