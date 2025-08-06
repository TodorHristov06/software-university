def even_numbers(function): 
    def wrapper(numbers): 
        result = function(numbers)
        return [number for number in result if number % 2 == 0]
    
    return wrapper