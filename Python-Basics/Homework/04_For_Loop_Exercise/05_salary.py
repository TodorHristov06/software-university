FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

number_of_tabs = int(input())
salary = int(input())
result = None

for _ in range(number_of_tabs):
    website = input()
    if website == "Facebook":
        salary -= FACEBOOK_FINE
    elif website == "Instagram":
        salary -= INSTAGRAM_FINE
    elif website == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        result = 'You have lost your salary.'
        break

else:
    result = salary

print(result)