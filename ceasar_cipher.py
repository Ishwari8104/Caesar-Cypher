alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(t, s):
  encoded_str = ""
  for n in t:
        old_index = alphabet.index(n)
        new_index = old_index + s
        encoded_str += alphabet[new_index]
  print("The encoded string is", encoded_str)
def decrypt(encoded_str,s):
   decoded_string=""
   for n in encoded_str:
        en_index = alphabet.index(n)
        de_index = en_index-s
        decoded_string+=alphabet[de_index]
   print("The decoded string is",decoded_string)
if direction=="encode":
    encrypt(t=text,s=shift)
else:
    decrypt(encoded_str=text,s=shift)
 