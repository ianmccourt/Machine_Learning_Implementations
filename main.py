# This program was created by: Ian McCourt

building_map = {
    "start": {"E": 1},
    1: {"E": 2},
    2: {"W": 1, "E": 3, "S": 4},
    3: {"W": 2},
    4: {"S": 6, "N": 2},
    5: {"E": 6},
    6: {"W": 5, "E": 7},
    7: {"W": 6, "E": "end"}
}

room_descriptions = {
    "start": "You're in the start room. You can only go East.",
    1: "You've walked into a room with a giant painting of a clown.",
    2: "You've entered a large hall with a sculpture of a Laker.",
    3: "You've stepped into a bedroom with bright pink walls.",
    4: "You've walked into a large room with a bunch of plants.",
    5: "You've entered a long room with dark green walls.",
    6: "You've walked into a room with a fireplace.",
    7: "You've reached the final room, but the door is locked. Do you have the key?"
}

current_room = "start"
has_key = False

while True:
    print(room_descriptions[current_room])

    if current_room == 7:
        if has_key:
            print("Congratulations! You've unlocked the door and exited the building.")
            break
        else:
            print("You need a key to exit. Find the key first.")

    if current_room == 5:
        if not has_key:
            pickup_key = input("There's a key on the floor. Would you like to pick it up? (yes/no): ").lower()
            if pickup_key == "yes":
                has_key = True
                print("You've picked up the key.")

    direction = input("Which door would you like to choose? (N, S, W, E): ").upper()

    if direction in building_map[current_room]:
        next_room = building_map[current_room][direction]
        current_room = next_room
    else:
        print("You can't go that way! Try a different door.")

print("Game over!")

