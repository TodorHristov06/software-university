MIN_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

result = ''

for _ in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())
    academy_points += len(judge_name) * judge_points / 2
    
    if academy_points > MIN_POINTS:
        result = f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!"
        break
    else:
        result = f"Sorry, {actor_name} you need {MIN_POINTS - academy_points:.1f} more!"

print(result)