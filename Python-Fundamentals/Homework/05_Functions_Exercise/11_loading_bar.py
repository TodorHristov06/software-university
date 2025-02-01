def loading_bar(percentage):
    if percentage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    
    loaded_percentage_as_digit = percentage // 10
    not_loaded_percentage_as_digit = 10 - loaded_percentage_as_digit
    return f"{percentage}% [{'%' * loaded_percentage_as_digit}{'.' * not_loaded_percentage_as_digit}]\nStill loading..."

number = int(input())

print(loading_bar(number))