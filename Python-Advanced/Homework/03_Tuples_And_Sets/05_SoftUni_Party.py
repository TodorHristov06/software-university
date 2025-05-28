n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    code = input()
    if code[0].isdigit():
        vip_guests.add(code)
    else:
        regular_guests.add(code)

while True:
    line = input()
    if line == "END":
        break
    if line in vip_guests:
        vip_guests.remove(line)
    elif line in regular_guests:
        regular_guests.remove(line)

print(len(vip_guests) + len(regular_guests))

for guest in sorted(vip_guests):
    print(guest)

for guest in sorted(regular_guests):
    print(guest)
