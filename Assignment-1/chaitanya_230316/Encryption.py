def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char == ' ':  # Don't encrypt spaces
            encrypted_message += char
        else:
            # Convert char to its numerical value, shift it by key, and convert it back to char
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_message += encrypted_char
    return encrypted_message

# Test cases
message_1 = 'iitk is better than iitd and iitb'
message_2 = 'lets learn cryptography'

encrypted_1 = encrypt(message_1, 9)
encrypted_2 = encrypt(message_2, 25)

print("Encrypted Message 1:", encrypted_1)
print("Encrypted Message 2:", encrypted_2)
