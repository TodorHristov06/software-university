def string_manipulator():
    string = input()
    
    while True:
        command = input()
        
        if command == "End":
            break
        
        command_parts = command.split()
        
        if command_parts[0] == "Translate":
            char = command_parts[1]
            replacement = command_parts[2]
            string = string.replace(char, replacement)
            print(string)
        
        elif command_parts[0] == "Includes":
            substring = command_parts[1]
            print("True" if substring in string else "False")
        
        elif command_parts[0] == "Start":
            substring = command_parts[1]
            print("True" if string.startswith(substring) else "False")
        
        elif command_parts[0] == "Lowercase":
            string = string.lower()
            print(string)
        
        elif command_parts[0] == "FindIndex":
            char = command_parts[1]
            print(string.rfind(char))
        
        elif command_parts[0] == "Remove":
            start_index = int(command_parts[1])
            count = int(command_parts[2])
            string = string[:start_index] + string[start_index + count:]
            print(string)

string_manipulator()
