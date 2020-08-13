# Create characters
class Player:
    def __init__(self, name):
        self.name = name
        self.attack_val = 10
        self.heal_val = 16
        self.health_val = 100

    def attack(self, enemy):
        enemy.health_val = enemy.health_val - self.attack_val
        print(enemy.name + "'s health is now " + str(enemy.health_val))

    def heal(self):
        self.health_val = self.health_val + player.heal_val
        print(player.name + "'s health is now " + str(player.health_val))


class Monster:
    def __init__(self):
        self.name ="Max"
        self.attack_val = 12
        self.health_val = 100

    def attack(self, enemy):
        enemy.health_val = enemy.health_val - self.attack_val
        print(self.name + " attacked! " + enemy.name + "'s health is now " + str(enemy.health_val))


# Get User's name
print("---" * 7)
player_name = input("What's your name: ")

while len(player_name) < 1:
    player_name = input("Please write a name: ")


# Init characters
player = Player(player_name)
monster = Monster()


# Game
game_running = True

while game_running:
    #Action selection
    print("Select an action")
    print("1 - Attack")
    print("2 - Heal")
    print("3 - Quit game")

    player_choice = input("What do you choose?: ")

    if player_choice == '3':
        print("Good bye!")
        game_running = False

    if player_choice == '1':
        player.attack(monster)
        if monster.health_val <= 0:
            print("You win!")
            game_running = False
        monster.attack(player)
        if player.health_val <= 0:
            print("You lost!")
            game_running = False


    if player_choice == '2':
        player.heal()
        if player.health_val >= 100:
            player.health_val = 100
        monster.attack(player)




