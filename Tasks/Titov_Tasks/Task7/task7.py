import random
import task7_maze as mz
from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def __init__(self, name, class_entity, damage, hp, lvl=1):
        self.__name = name
        self.__class_entity = class_entity
        self.__damage = damage
        self.__hp = hp
        self.__lvl = lvl

    @abstractmethod
    def get_name(self):
        return self.__name

    @abstractmethod
    def get_class_entity(self):
        return self.__class_entity

    @abstractmethod
    def get_damage(self):
        return self.__damage

    @abstractmethod
    def get_hp(self):
        return self.__hp

    @abstractmethod
    def get_lvl(self):
        return self.__lvl

    def attack(self):
        attacks_types = random.choice(["basic attack", "critical hit"])
        if attacks_types == "basic attack":
            print(f"{self.get_name()} basic attack")
            return self.__damage * self.__lvl
        else:
            print(f"{self.get_name()} critical hit")
            return self.__damage * self.__lvl * 2

    @staticmethod
    def do_attack(hero, curr_hp_hero, monster):
        curr_hp_monster = monster.get_hp() - hero.attack()
        if curr_hp_monster > 0:
            curr_hp_hero -= monster.attack()
            if curr_hp_hero > 0:
                while curr_hp_monster > 0 or curr_hp_hero > 0:
                    curr_hp_monster -= hero.attack()
                    if curr_hp_monster <= 0:
                        break
                    curr_hp_hero -= monster.attack()
                    if curr_hp_hero <= 0:
                        break
            else:
                print("You died. Game over")
        if curr_hp_monster <= 0:
            print("You Win")
            print("You remaining Hp", curr_hp_hero)
        else:
            print("You died. Game over")
            print("Monster remaining Hp", curr_hp_monster)
        return curr_hp_hero

    def start_room(self, room_exits):
        start_room = random.choice(list(room_exits.keys()))
        print(f"{self.get_name()} start:", start_room)
        return start_room

    @staticmethod
    def move(room_exits, curr_room):
        curr_room = random.choice(room_exits.get(curr_room))
        return curr_room


class Hero(Entity):

    def __init__(self, name, class_entity, damage, hp, lvl=1):
        super().__init__(name, class_entity, damage, hp, lvl)

    def get_name(self):
        return super().get_name()

    def get_class_entity(self):
        return super().get_class_entity()

    def get_damage(self):
        return super().get_damage()

    def get_hp(self):
        return super().get_hp()

    def get_lvl(self):
        return super().get_lvl()


class Monster(Entity):

    def __init__(self, name, class_entity, damage, hp, lvl=1):
        super().__init__(name, class_entity, damage, hp, lvl)

    def get_name(self):
        return super().get_name()

    def get_class_entity(self):
        return super().get_class_entity()

    def get_damage(self):
        return super().get_damage()

    def get_hp(self):
        return super().get_hp()

    def get_lvl(self):
        return super().get_lvl()


rooms1 = mz.maze1.get_rooms()
print("Maze:")
mz.maze1.print_maze()


hero1 = Hero("Gopher", "warrior", 50, 1000)
print("Hero:", hero1.get_name(), hero1.get_class_entity(),
      hero1.get_damage(),
      hero1.get_hp(), hero1.get_lvl())

monster1 = Monster("Flame", "dragon", 15, 500, 8)
print("Monster:", monster1.get_name(), monster1.get_class_entity(),
      monster1.get_damage(),
      monster1.get_hp(), monster1.get_lvl())

start_room_hero = hero1.start_room(rooms1)
start_room_monster = monster1.start_room(rooms1)
while start_room_hero == start_room_monster:
    start_room_monster = monster1.start_room(rooms1)

moves_hero, moves_monster = [], []                # for movement visualization
moves_hero.append(start_room_hero)
moves_monster.append(start_room_monster)
curr_room_hero = hero1.move(rooms1, start_room_hero)
moves_hero.append(curr_room_hero)
curr_room_monster = monster1.move(rooms1, start_room_monster)
moves_monster.append(curr_room_monster)
while curr_room_hero != curr_room_monster:
    curr_room_hero = hero1.move(rooms1, curr_room_hero)
    moves_hero.append(curr_room_hero)
    if curr_room_hero != curr_room_monster:
        curr_room_monster = monster1.move(rooms1, curr_room_monster)
        moves_monster.append(curr_room_monster)
    else:
        break
print("Hero moves:", moves_hero)
print("Monster moves:", moves_monster)

hero1.do_attack(hero1, hero1.get_hp(), monster1)
