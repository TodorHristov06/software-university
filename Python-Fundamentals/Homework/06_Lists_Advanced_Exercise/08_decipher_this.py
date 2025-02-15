def decipher_word(word):
    num_part = ""
    char_part = ""
    
    for char in word:
        if char.isdigit():
            num_part += char
        else:
            char_part += char

    first_letter = chr(int(num_part))

    if len(char_part) > 1:
        char_part = char_part[-1] + char_part[1:-1] + char_part[0]

    return first_letter + char_part

def decipher_message(message):
    words = message.split()
    deciphered_words = []

    for word in words:
        deciphered_words.append(decipher_word(word))

    return " ".join(deciphered_words)

message = input()
print(decipher_message(message))
