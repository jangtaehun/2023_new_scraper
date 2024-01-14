"""
class Puppy:
    def __init__(self, name, feed):
        self.name = name
        self.age = 5
        self.feed = feed
    def __str__(self):
        return f"cat named {self.name}, age {self.age}, feed {self.feed}"
    def woof_woof(self):
        print("woof")
    def introduce(self):
        self.woof_woof() #클래스 안에 있는 메소드는 다른 메소드를 호출할 수 있다.
        print(f'my name {self.name}')

ruffus = Puppy(name = "zzone", feed = "fish")
bibi = Puppy(name = "ddeock", feed = "fish")

ruffus.woof_woof()
ruffus.introduce()
bibi.introduce()
print(ruffus.name, ruffus.age, ruffus.feed)
print(ruffus)
print(bibi)

class guard_dog:
    def __init__(self, name, feed):
        self.name = name
        self.feed = feed
        self.age = 5
    def rrrr(self):
        print("stay away")
    def __str__(self):
        return f"my name {self.name}, age {self.age}, feed {self.feed}"
        
king_zzone = guard_dog("King_zzone", "shark")
print(king_zzone)
"""


#inheritance = 상속
# Puppy와 guard_dog는 모두 name, feed, age를 갖는다.
# super => 부모의 class를 참조
"""
class Dog:
    def __init__(self, name, feed, age):
        self.name = name
        self.feed = feed
        self.age = age
    def sleep(self):
        print("zzzz...")
    def introduce(self):
        print(f'cat named {self.name}, age {self.age}, feed {self.feed}')


class Puppy(Dog):
    def __init__(self, name, feed):
        super().__init__(name, feed, 3)
        self.spoiled = True
    def woof_woof(self):
        print("woof")


class guard_dog(Dog):
    def __init__(self, name, feed):
        super().__init__(name, feed, 5)
        self.aggressive = True
    def rrrr(self):
        print("stay away")


ruffus = Puppy(name = "zzone", feed = "fish")
bibi = guard_dog(name = "ddeock", feed = "fish")

Dog(name = "zzone", feed = "fish", age=5).sleep()
Dog(name = "zzone", feed = "fish", age=5).introduce()

ruffus.woof_woof()
bibi.rrrr()

ruffus.sleep()
bibi.sleep()

print(ruffus.name, ruffus.age)
print(bibi.name, bibi.age)
"""


#player 삭제하는 메소드
#팀의 경험치의 총합을 보여주는 메소드
class Player:
    def __init__(self, name, team, xp):
        self.name = name
        self.team = team
        self.xp = xp
    def introduce(self):
        print(f'Hello i am {self.name}. and i play for {self.team}')


class Team(Player):
    def __init__(self, name, team, xp):
        super().__init__(name, team, xp)
        self.players = []

    def add_player(self):
        new_player = Player(self.name, self.team, self.xp)
        self.players.append(new_player)
        print(f"i'm {self.name}")

    def show_players(self):
        print(self.players)
        for player in self.players:
               player.introduce()


    def delete(self, name):
        for player in self.players:
            if name in player.name:
                del player.name
                del player.team
                del player.xp

    def total(self):
        total_xp = 0
        for player in self.players:
            total_xp += self.xp
        print(total_xp)


h1 = Team(name='zzoneddeock', team='cat', xp=1000)
h2 = Team(name='DD', team='cat', xp=1000)

h1.add_player()
h1.show_players()
print()

h1.delete('zzoneddeock')
print()
h1.show_players()
