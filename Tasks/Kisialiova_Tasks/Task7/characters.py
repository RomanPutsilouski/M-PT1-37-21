import random
from abc import ABC, abstractmethod

from Tasks.Kisialiova_Tasks.Task7.maze import DIRECTIONS


class Character(ABC):

    @abstractmethod
    def __init__(self, name, health, damage, level=1):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def get_damage(self):
        return self.damage

    @abstractmethod
    def get_health(self):
        return self.health

    @abstractmethod
    def get_level(self):
        return self.level

    def attack(self, enemy):
        enemy.health -= self.damage
        print(f'{self.name} attacks {enemy.name} with {self.damage} damage')

    def defend(self):
        pass

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False


class Hero(Character):

    def __init__(self, name, level, health, damage, class_):
        super().__init__(name, level, health, damage)
        self.class_ = class_

    def get_name(self):
        return super().get_name()

    def get_damage(self):
        return super().get_damage()

    def get_health(self):
        return super().get_health()

    def get_level(self):
        return super().get_level()


class Monster(Character):
    def __init__(self, name, level, health, damage, race):
        super().__init__(name, level, health, damage)
        self.race = race

    def get_name(self):
        return super().get_name()

    def get_damage(self):
        return super().get_damage()

    def get_health(self):
        return super().get_health()

    def get_level(self):
        return super().get_level()


class PositionInMaze:
    def __init__(self, maze, position):
        self.maze = maze
        self.position = position

    def __eq__(self, other):
        if self.maze is other.maze and self.position == other.position:
            return True
        else:
            return False

    @classmethod
    def create_random(cls, maze):
        room_coords = maze.rooms.keys()
        random_coords = random.choice(list(room_coords))
        return cls(maze=maze, position=random_coords)

    def get_current_room(self):
        return self.maze.rooms[self.position]

    def get_possible_directions(self):
        room = self.get_current_room()
        return room.get_passable_directions()

    def move_direction(self, direction):
        if direction in self.get_possible_directions():
            current_room = self.get_current_room()
            door = getattr(current_room, direction)
            new_room = door.room_behind(current_room)
            new_coords = self.maze.get_room_coords(new_room)
            self.position = new_coords


class CharacterInMaze:
    def __init__(self, character, character_position):
        self.character = character
        self.character_position = character_position

    def move(self, direction):
        self.character_position.move_direction(direction)
        print('Character {} moved to {} ({})'.format(self.character.name, direction, self.character_position.position))

    def random_move(self):
        possible_directions = self.character_position.get_possible_directions()
        self.move(random.choice(possible_directions))


class CharacterSpawner:
    def __init__(self, maze):
        self.maze = maze

    def spawn_random_monster(self):
        character = Monster(name='Skeleton', level=1, health=3, damage=1, race='Undead')
        position = PositionInMaze.create_random(self.maze)
        character_in_maze = CharacterInMaze(character=character, character_position=position)
        print(f'{character.name} spawned at ({position.position})')
        return character_in_maze

    def spawn_hero(self):
        character = Hero(name='Gerald', level=10, health=20, damage=2, class_='Warrior')
        position = PositionInMaze.create_random(self.maze)
        character_in_maze = CharacterInMaze(character=character, character_position=position)
        print(f'{character.name} spawned at ({position.position})')
        return character_in_maze


class BattleFinished(Exception):
    pass


class CharacterInMazeProcessor:
    def __init__(self, characters):
        self.characters = characters

    def characters_in_the_same_room(self):
        positions = [x.character_position for x in self.characters]
        if positions[0] == positions[1]:
            return True
        else:
            return False

    def process(self):
        for character in self.characters:
            if self.characters_in_the_same_room():
                battle_resolver = BattleResolver([x.character for x in self.characters])
                battle_resolver.resolve()
                raise BattleFinished
            character.random_move()

    def process_cycle(self):
        counter = 1
        while True:
            print(f'Turn {counter}')
            try:
                self.process()
            except BattleFinished:
                break
            counter += 1


class BattleResolver:
    def __init__(self, characters):
        self.character1 = characters[0]
        self.character2 = characters[1]

    def winner(self):
        if self.character1.is_dead() and self.character2.is_dead():
            return 'No winner'
        elif self.character1.is_dead():
            return self.character2
        elif self.character2.is_dead():
            return self.character1
        else:
            return None

    def resolve(self):
        print(f'Battle begins: {self.character1.name} vs {self.character2.name}')
        while not self.winner():
            self.attack_each_other()
        else:
            if self.winner == 'No winner':
                print('Draw! All characters are dead!')
            else:
                print(f'{self.winner().name} wins!')

    def attack_each_other(self):
        self.character1.attack(self.character2)
        self.character2.attack(self.character1)
