# Task 01- Caesar Cipher Encryption and Decryption
# Cybersecurity Internship - SkillCraft Technology
# Description- This program encrypts and decrypts a message using the Caesar Cipher algorithm . 
# The user enters a message and shift value, and the program outputs the encrypted and decrypted the text.  
def encrypt(text,shift):
 result = ""

 for char in text:
  if char.isalpha():
   if char.isupper():
    result += chr((ord(char)- 65 + shift) % 26 + 65)
   else:
    result += chr((ord(char) - 97 + shift) % 26 + 97)
  else:
   result += char
 
 return result

def decrypt(text,shift):
 return encrypt(text, -shift)

print("=== Caesar Cipher Tool ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(message, shift)
print("Encrypted Message:",encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Message:", decrypted_text)
