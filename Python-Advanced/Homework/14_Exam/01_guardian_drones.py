parts = list(map(int, input().split()))
cells = list(map(int, input().split()))

drones = {
    'Sentinel-X': 100,
    'Viper-MKII': 85,
    'Aegis-7': 75,
    'Striker-R': 65,
    'Titan-Core': 55
}

assembled = []
assembled_names = set()

while parts and cells and len(assembled) < 5:
    current_part = parts[-1]
    current_cell = cells[0]
    total = current_part + current_cell
    
    exact_match = None
    for name, power in drones.items():
        if power == total and name not in assembled_names:
            exact_match = name
            break
    
    if exact_match:
        assembled.append(exact_match)
        assembled_names.add(exact_match)
        parts.pop()
        cells.pop(0)
    else:
        possible_drones = []
        for name, power in drones.items():
            if power < total and name not in assembled_names:
                possible_drones.append((power, name))
        
        if possible_drones:
            possible_drones.sort(reverse=True)
            selected_power, selected_name = possible_drones[0]
            assembled.append(selected_name)
            assembled_names.add(selected_name)
            parts.pop()

            new_cell = current_cell - 30
            cells.pop(0)
            if new_cell > 0:
                cells.append(new_cell)
        else:
            parts.pop()
            cells.pop(0)
            new_cell = current_cell - 1
            if new_cell > 0:
                cells.append(new_cell)

if len(assembled) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled:
    print("Assembled Drones: " + ", ".join(assembled))

if parts:
    print("Mechanical Parts: " + ", ".join(map(str, reversed(parts))))
if cells:
    print("Power Cells: " + ", ".join(map(str, cells)))