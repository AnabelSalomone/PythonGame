player = {
    "name": "",
    "attack": 10,
    "heal": 16,
    "health": 100
}

monster = {
    "name": "Max",
    "attack": 12,
    "health": 100
}

# Get User's name
print("---" * 7)
player["name"] = input("What's your name: ")

while len(player["name"]) < 1:
    player["name"] = input("Please write a name: ")


# Game
game_running = True

def player_attack():
    monster["health"] = monster["health"] - player["attack"]

while game_running:
    #Action selection
    print("Select an action")
    print("1 - Attack")
    print("2 - Heal")
    print("3 - Quit game")
    print("---" * 7)

    player_choice = input("What do you choose?")

    if player_choice == '3':
        print("Good bye!")
        game_running = False

    if player_choice == '1':
        player_attack()
        print (monster["health"])




