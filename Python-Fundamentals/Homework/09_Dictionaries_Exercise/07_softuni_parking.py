n = int(input())
parking_lot = {}

for _ in range(n):
    command = input().split()
    action, username = command[0], command[1]
    
    if action == "register":
        license_plate = command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    
    elif action == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for user, plate in parking_lot.items():
    print(f"{user} => {plate}")