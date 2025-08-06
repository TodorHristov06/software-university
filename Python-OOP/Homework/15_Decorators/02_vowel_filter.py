def vowel_filter(function): 
    def wrapper(): 
        vowels = 'aeiou'
        result = function()
        return [char for char in result if char.lower() in vowels]
    return wrapper

@vowel_filter
def get_letters():
    return 'aeiouy'

print(get_letters())