class Labirint:

    def __init__(self, rooms, current_room):
        self.rooms = rooms
        self.current_room = current_room

    def next_room(self, hero, monster):
        reachable_rooms = self.rooms.get(self.current_room.name)
        if not reachable_rooms:
            return True
        print(f"{hero.name} doesn't find {monster.name} in {self.current_room.name}. Choose the next room: {[room.name for room in reachable_rooms]}.")
        while True:
            a = input("Enter the next room:\n")
            for room in reachable_rooms:
                if a == room.name:
                    room.handle_hero(hero)
                    self.current_room = room
                    return False
            print(f"Slected room is not reachable from current room!") 

class Room:
    
    def __init__(self, name, bonus, force, monster):
        self.name = name
        self.bonus = bonus
        self.monster = monster
        self.force = force

    def handle_hero(self, hero):
        if self.bonus == "armour":
            print(f"\nGood job! {hero.name} armour was upgraded!")
            hero.add_bonus(self.bonus)
            self.bonus = None
        if self.bonus == "power":
            print(f"\nCongratulations! {hero.name} find extra power!")
            hero.add_bonus(self.bonus)
            self.bonus = None
        if self.monster is not None:
            TheEnd.fight(hero, self)
            self.monster = None
        if self.force is not None:
            if "armour" in hero.bonus:
                print(f"\n{hero.name} faced with a negative force and lost his upgraded armour!")
                hero.bonus.remove("armour")
            else:
                print(f"Suddenly {hero.name} faced with a negative force and lost his power!")
                hero.bonus.remove("power")
                self.force = None



class Hero:

    def __init__(self, name):
        self.name = name
        self.bonus = list()
    
    def add_bonus(self, bonus):
        self.bonus.append(bonus)

class Monster:

    def __init__(self, name):
        self.name = name

class TheEnd:

    @staticmethod
    def end(decision, room):
        if decision == 1:
            print(f"Well done! {hero.name} defeat Monster!")
            room.monster = None
            room = None
        elif decision == 2:
            print(f"{hero.name} let {monster.name} leave! Very merciful!")
        else:
            TheEnd.end(input("Please enter the right choice:\n"), room)

    @staticmethod
    def fight(hero, room):
        print(f"{hero.name} find Monster!")
        if "power" in hero.bonus:
            print(f"{hero.name} have an extra power to defeat {monster.name} but also can let him leave!")
            TheEnd.end(int(input("Choose defeat(1) or let leave(2) (press 1 or 2):\n")), room)
        else:
            print(f"{hero.name} doesn't have enough power and health to defeat {monster.name}! {monster.name} defeat {hero.name}!")

room1 = Room("room1", None, None, None)
room2 = Room("room2", None, None, None)
room3 = Room("room3", "armour", None, None)
room4 = Room("room4", "power", None, None)
room5 = Room("room5", None, None, None)
room6 = Room("room6", None, None, None)
room7 = Room("room7", None, "negative force", None)
room8 = Room("room8", None, None, None)
room9 = Room("room9", None, None, None)
room10 = Room("room10", None, None, "monster")

labirint = Labirint({
    "room1": [room2],
    "room2": [room1, room3, room4],
    "room3": [room2, room6],
    "room4": [room2, room5, room6, room7],
    "room5": [room4],
    "room6": [room3, room4, room8],
    "room7": [room4],
    "room8": [room6, room9],
    "room9": [room8, room10],
    "room10": []
    }, room1)

hero = Hero("Terminator")
monster = Monster("Alien")

while True:
    if labirint.next_room(hero, monster):
        break