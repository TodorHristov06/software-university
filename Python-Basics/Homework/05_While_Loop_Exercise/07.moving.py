width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
volume_of_free_space = width_of_free_space * length_of_free_space * height_of_free_space

cubic_meters = 0
result = ''

while volume_of_free_space > cubic_meters:
    command = input()
    
    if command == 'Done':
        result = f'{volume_of_free_space - cubic_meters} Cubic meters left.'
        break

    cubic_meters += int(command)
else:
    result = f'No more free space! You need {abs(cubic_meters - volume_of_free_space)} Cubic meters more.'

print(result)

