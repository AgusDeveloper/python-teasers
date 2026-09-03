class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1

p1 = Player("God, all my virgins, saints, angels and Family")
print(Player.count)
print(p1.count)
p2 = Player("Love so much")
print(p2.count)
