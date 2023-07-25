import time

# Define the rooms and their connections
rooms = {
    'entrance': {'east': 'living_room'},
    'living_room': {'west': 'entrance', 'south': 'kitchen'},
    'kitchen': {'north': 'living_room', 'east': 'bedroom'},
    'bedroom': {'west': 'kitchen'}
}

# Define the items in each room
items = {
    'entrance': ['key'],
    'living_room': ['couch', 'remote'],
    'kitchen': ['knife'],
    'bedroom': ['book']
}

# Player's inventory
inventory = []

def display_room(room_name):
    print(f"You are in the {room_name.capitalize()}.")
    if room_name in items:
        print("You see the following items:")
        for item in items[room_name]:
            print(f" - {item}")

def move_to_room(current_room, direction):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way.")
        return current_room

def main():
    print("Welcome to the Text Adventure Game!")
    print("Type 'exit' to quit the game at any time.\n")
    
    current_room = 'entrance'
    
    while True:
        display_room(current_room)
        if current_room == 'bedroom' and 'key' in inventory:
            print("Congratulations! You found the key and unlocked the bedroom door. You win!")
            break
        
        command = input("\nWhat do you want to do? ").lower()
        
        if command == 'exit':
            print("Thanks for playing. See you next time!")
            break
        elif command.startswith('go '):
            direction = command[3:]
            current_room = move_to_room(current_room, direction)
        elif command.startswith('take '):
            item = command[5:]
            if item in items[current_room]:
                items[current_room].remove(item)
                inventory.append(item)
                print(f"You picked up {item}.")
            else:
                print("That item is not in this room.")
        elif command.startswith('inventory'):
            if inventory:
                print("You are carrying:")
                for item in inventory:
                    print(f" - {item}")
            else:
                print("Your inventory is empty.")
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
