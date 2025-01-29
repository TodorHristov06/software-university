fires_with_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells = []

for fire in fires_with_cells:
    fire_type, fire_value = fire.split(" = ")
    fire_value = int(fire_value)

    if fire_type == "High" and 81 <= fire_value <= 125:
        if water >= fire_value:
            water -= fire_value
            effort += fire_value * 0.25
            total_fire += fire_value
            cells.append(fire_value)
    elif fire_type == "Medium" and 51 <= fire_value <= 80:
        if water >= fire_value:
            water -= fire_value
            effort += fire_value * 0.25
            total_fire += fire_value
            cells.append(fire_value)
    elif fire_type == "Low" and 1 <= fire_value <= 50:
        if water >= fire_value:
            water -= fire_value
            effort += fire_value * 0.25
            total_fire += fire_value
            cells.append(fire_value)

print("Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

