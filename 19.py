inventory = { "apples": 50,"bananas": 100,"oranges": 75}

def update_inventory(inventory, item, quantity_change):
    if item in inventory:
        inventory[item] += quantity_change
    else:
        inventory[item] = quantity_change
    return inventory

inventory = update_inventory(inventory, "apples", 20)
inventory = update_inventory(inventory, "bananas", -24)

for item, quantity in inventory.items():
    print(f"{item}: {quantity}")