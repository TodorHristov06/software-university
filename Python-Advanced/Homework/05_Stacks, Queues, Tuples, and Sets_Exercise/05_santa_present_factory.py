from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

presents_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while materials and magic:
    material = materials[-1]
    mag = magic[0]

    if material == 0 and mag == 0:
        materials.pop()
        magic.popleft()
        continue
    elif material == 0:
        materials.pop()
        continue
    elif mag == 0:
        magic.popleft()
        continue

    product = material * mag

    if product in presents_magic:
        present = presents_magic[product]
        crafted_presents[present] = crafted_presents.get(present, 0) + 1
        materials.pop()
        magic.popleft()
    elif product < 0:
        materials.pop()
        magic.popleft()
        materials.append(material + mag)
    else:
        magic.popleft()
        materials[-1] += 15

success = (
    ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or
    ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)
)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy in sorted(crafted_presents):
    print(f"{toy}: {crafted_presents[toy]}")
