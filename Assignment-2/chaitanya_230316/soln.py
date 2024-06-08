import string
from collections import Counter
from itertools import cycle

# English letter frequencies
letter_freq = {'A': 0.0817, 'B': 0.0149, 'C': 0.0278, 'D': 0.0425,
               'E': 0.1270, 'F': 0.0223, 'G': 0.0202, 'H': 0.0609,
               'I': 0.0697, 'J': 0.0015, 'K': 0.0077, 'L': 0.0403,
               'M': 0.0241, 'N': 0.0675, 'O': 0.0751, 'P': 0.0193,
               'Q': 0.0010, 'R': 0.0599, 'S': 0.0633, 'T': 0.0906,
               'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015,
               'Y': 0.0197, 'Z': 0.0007}

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def bytes_to_hex(byte_str):
    return byte_str.hex()

def xor_decrypt(ciphertext, key):
    return bytes([c ^ k for c, k in zip(ciphertext, cycle(key))])

def calculate_letter_frequencies(text):
    letter_count = Counter(text)
    total_count = sum(letter_count.values())
    frequencies = {letter: count / total_count for letter, count in letter_count.items()}
    return frequencies

def guess_key(ciphertext, key_length):
    sections = [ciphertext[i::key_length] for i in range(key_length)]
    key = b''
    for section in sections:
        best_score = float('inf')
        best_key = b''
        for candidate_key in range(256):
            decrypted = xor_decrypt(section, bytes([candidate_key]))
            decrypted_freq = calculate_letter_frequencies(decrypted)
            score = sum((decrypted_freq.get(letter, 0) - letter_freq.get(chr(letter).upper(), 0))**2 for letter in range(256))
            if score < best_score:
                best_score = score
                best_key = bytes([candidate_key])
        key += best_key
    return key

def vigenere_like_crack(ciphertext_hex, max_key_length=10):
    ciphertext = hex_to_bytes(ciphertext_hex)
    best_key = b''
    best_score = float('inf')
    for key_length in range(1, max_key_length + 1):
        key = guess_key(ciphertext, key_length)
        decrypted = xor_decrypt(ciphertext, key)
        decrypted_freq = calculate_letter_frequencies(decrypted)
        score = sum((decrypted_freq.get(ord(letter), 0) - letter_freq.get(letter, 0))**2 for letter in string.ascii_uppercase)
        if score < best_score:
            best_score = score
            best_key = key
    return best_key

# Example usage
ciphertext_hex = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
key = vigenere_like_crack(ciphertext_hex)
decrypted = xor_decrypt(hex_to_bytes(ciphertext_hex), key)
print("Decrypted text:", decrypted.decode('utf-8'))
print("Key:", bytes_to_hex(key))
