def train_operations(n, commands):
    train = [0] * n
    
    for command in commands:
        parts = command.split()
        action = parts[0]
        
        if action == "add":
            people = int(parts[1])
            train[-1] += people
        elif action == "insert":
            index, people = int(parts[1]), int(parts[2])
            train[index] += people
        elif action == "leave":
            index, people = int(parts[1]), int(parts[2])
            train[index] -= people
    
    return train

n = int(input())
commands = []
while True:
    command = input()
    if command == "End":
        break
    commands.append(command)

print(train_operations(n, commands))