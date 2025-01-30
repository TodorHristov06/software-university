def process_commands(lst):
    while True:
        command = input().split()
        if command[0] == "end":
            print(f"[{', '.join(map(str, lst))}]")
            break
        
        if command[0] == "exchange":
            index = int(command[1])
            if 0 <= index < len(lst):
                lst = lst[index + 1:] + lst[:index + 1]
            else:
                print("Invalid index")
        
        elif command[0] == "max":
            even_odd = command[1]
            if even_odd == "even":
                valid_elements = [i for i in range(len(lst)) if lst[i] % 2 == 0]
            else:
                valid_elements = [i for i in range(len(lst)) if lst[i] % 2 != 0]
            
            if valid_elements:
                max_value = max(lst[i] for i in valid_elements)
                print(len(lst) - 1 - lst[::-1].index(max_value))
            else:
                print("No matches")
        
        elif command[0] == "min":
            even_odd = command[1]
            if even_odd == "even":
                valid_elements = [i for i in range(len(lst)) if lst[i] % 2 == 0]
            else:
                valid_elements = [i for i in range(len(lst)) if lst[i] % 2 != 0]
            
            if valid_elements:
                min_value = min(lst[i] for i in valid_elements)
                print(len(lst) - 1 - lst[::-1].index(min_value))
            else:
                print("No matches")
        
        elif command[0] == "first":
            count = int(command[1])
            even_odd = command[2]
            if count > len(lst):
                print("Invalid count")
            else:
                if even_odd == "even":
                    result = [x for x in lst if x % 2 == 0][:count]
                else:
                    result = [x for x in lst if x % 2 != 0][:count]
                print(result)
        
        elif command[0] == "last":
            count = int(command[1])
            even_odd = command[2]
            if count > len(lst):
                print("Invalid count")
            else:
                if even_odd == "even":
                    result = [x for x in lst if x % 2 == 0][-count:]
                else:
                    result = [x for x in lst if x % 2 != 0][-count:]
                print(result)

lst = list(map(int, input().split()))

process_commands(lst)