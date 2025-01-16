WORDS = ["sand", "water", "fish", "sun"]
input_string = input().lower()
words_count = 0

for word in WORDS:
    words_count += input_string.count(word)

print(words_count)