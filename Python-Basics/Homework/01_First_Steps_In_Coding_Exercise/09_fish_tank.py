length = float(input())
width = float(input())
height = float(input())
percentage = float(input()) / 100

volume = length * width * height
volume_in_liters = volume * 0.001
percentage_in_liters = volume_in_liters * percentage
needed_liters = volume_in_liters - percentage_in_liters

print(needed_liters)