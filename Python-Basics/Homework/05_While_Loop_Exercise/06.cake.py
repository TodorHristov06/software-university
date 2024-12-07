length = int(input())
width = int(input())

cake = length * width
pieces = 0
command = input()

while command != "STOP":
    pieces += int(command)
    if pieces > cake:
        print(f"No more cake left! You need {pieces - cake} pieces more.")
        break
    command = input()

else:
    print(f"{cake - pieces} pieces are left.")