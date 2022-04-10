inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
def displayInventory():
    amount = list(inventory)
    print('Inventory:')
    print(str(inventory['arrow']) + ' arrows.')
    print(str(inventory['gold coin']) + ' gold coins.')
    print(str(inventory['rope']) + ' rope.')
    print(str(inventory['torch']) + ' torches.')
    print(str(inventory['dagger']) + ' daggers.')
    total = 0
    for k, v in inventory.items():
        total += v
    print('Total number of items: ' + str(total))
displayInventory()