def caesar_decrypt(encrypted_message, key):
    decrypted_message = []
    for char in encrypted_message:
        if char == ' ':
            decrypted_message.append(char)
        else:
            decrypted_char = chr((ord(char) - ord('a') - key + 26) % 26 + ord('a'))
            decrypted_message.append(decrypted_char)
    return ''.join(decrypted_message)

def is_intelligible(text, common_words):
    word_list = text.split()
    return sum(word in common_words for word in word_list)

def find_most_probable_message(encrypted_message, common_words):
    possible_messages = []
    
    for key in range(26):
        decrypted_message = caesar_decrypt(encrypted_message, key)
        possible_messages.append(decrypted_message)
    
    # Find the most probable message by checking for intelligibility
    most_probable_message = ""
    max_intelligible_words = 0
    
    for message in possible_messages:
        intelligible_words = is_intelligible(message, common_words)
        
        if intelligible_words > max_intelligible_words:
            max_intelligible_words = intelligible_words
            most_probable_message = message
            
    return most_probable_message, possible_messages

# Define a small list of common English words
common_words = set([
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
    'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
    'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there',
    'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',
    'which', 'go', 'me'
])

# Example usage
encrypted_message_1 = 'bm ptl wtfg xtlr tztbg'
encrypted_message_2 = 'rc fjb mjvw njbh'

most_probable_message_1, possible_messages_1 = find_most_probable_message(encrypted_message_1, common_words)
most_probable_message_2, possible_messages_2 = find_most_probable_message(encrypted_message_2, common_words)

print("Most Probable Message 1:", most_probable_message_1)
print("All Possible Messages 1:", possible_messages_1)
print("Most Probable Message 2:", most_probable_message_2)
print("All Possible Messages 2:", possible_messages_2)
