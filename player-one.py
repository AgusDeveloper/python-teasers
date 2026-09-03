class Player:
    count = 0
    def __init__(self, name):
        self.name = name
        self.count += 1

p1 = Player("God, all my virgins, saints and angels,")
print(Player.count)