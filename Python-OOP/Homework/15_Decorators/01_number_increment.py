def number_increment(numbers):
    def increase(): 
        return [number + 1 for number in numbers]
    
    return increase()