searched_book = input()

book_count = 0
result = ""

while True:
    book_name = input()
    
    if book_name == "No More Books":
        result = f'The book you search is not here!\nYou checked {book_count} books.'
        break
    
    if book_name == searched_book:
        result = f"You checked {book_count} books and found it."
        break
    
    book_count += 1

print(result)