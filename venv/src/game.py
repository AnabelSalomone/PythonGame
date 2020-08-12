player = {
    "name": "Player 1",
    "attack": 10,
    "heal": 16,
    "health": 100
}

monster = {
    "name": "Max",
    "attack": 12,
    "health": 100
}

#Get User's name
player["name"] = input("What's your name: ")

while len(player["name"]) < 1:
    player["name"] = input("Please write a name: ")


#Action selection
print("Select an action")
print("1 - Attack")
print("2 - Heal")

player_choice = input("What do you choose?")

