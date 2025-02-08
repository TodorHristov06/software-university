def remove_vowels(word):
    vowels = ["a","o","u","e","i"]
    result = ''.join([char for char in word if char.lower() not in vowels])
    return result

word = input()
print(remove_vowels(word))