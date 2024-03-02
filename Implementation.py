
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


print(" Hello MR/Mis")
user_choice = input(" Please enter type operation: Encrypt / Decrypt\n")

plain_text = input(" Enter the plain text (Work): ")
shift_value = int(input(" Enter the shift number: "))

if user_choice.lower() == "encrypt" or user_choice.lower() == "encrypted":
    encrypted_text = caesar_cipher(plain_text, shift_value)
    print("Cipher text is:", encrypted_text)
elif user_choice.lower() == "decrypt" or user_choice.lower() == "decrypted":
    decrypted_text = caesar_cipher(plain_text, -shift_value)
    print("Plain text is:", decrypted_text)
else:
    print("Invalid input")