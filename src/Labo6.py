import sys

# Functie om de lijst van items bij te houden
def manage_list(action, item, items_list):
    if action == 'Server toevoegen':
        items_list.append(item)
    elif action == 'Server verwijderen':
        if item in items_list:
            items_list.remove(item)
    elif action == 'Server lijst tonen':
        print(items_list)

# Als er geen argumenten zijn, vraag de gebruiker om invoer
if len(sys.argv) == 1:
    action = input("Kies actie (Server toevoegen/Server verwijderen/Server lijst tonen): ")
    server = input("Voer server in: ")
else:
    action = sys.argv[1]
    server = sys.argv[2]

# Lijst van items
items_list = ['item 1', 'item 2', 'item 3']

# Beheer van de lijst afhankelijk van de gekozen actie
manage_list(action, server, items_list)
