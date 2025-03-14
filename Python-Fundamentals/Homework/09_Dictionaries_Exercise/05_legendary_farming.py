materials = {"shards": 0, "fragments": 0, "motes": 0}
won_legendary_item = False
legendary_item = ""
while not won_legendary_item:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        key = current_items[index + 1].lower()
        value = int(current_items[index])

        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            legendary_item = "Shadowmourne"
            won_legendary_item = True
            materials["shards"] -= 250
        elif materials["fragments"] >= 250:
            legendary_item = "Valanyr"
            won_legendary_item = True
            materials["fragments"] -= 250
        elif materials["motes"] >= 250:
            legendary_item = "Dragonwrath"
            won_legendary_item = True
            materials["motes"] -= 250
        if won_legendary_item:
            break
print(f"{legendary_item} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")
