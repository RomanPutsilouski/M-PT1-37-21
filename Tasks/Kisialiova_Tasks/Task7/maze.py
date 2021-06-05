import random
from itertools import starmap
from operator import add

DIRECTIONS = ('east', 'west', 'south', 'north')


def add_m(*args):
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


class Wall:
    passable = False


class Door:
    passable = True

    def __init__(self, rooms):
        self.rooms = rooms

    def room_behind(self, room_from):
        rooms = list(self.rooms)
        rooms.remove(room_from)
        return rooms[0]


class Room:

    def __init__(self, east, west, north, south):
        self.east = east
        self.west = west
        self.north = north
        self.south = south

    @classmethod
    def create_with_walls(cls):
        walls = [Wall() for _ in range(4)]
        return cls(*walls)

    def set_direction(self, direction, obj):
        if direction in DIRECTIONS:
            setattr(self, direction, obj)

    def get_passable_directions(self):
        passable_directions = []
        for direction in DIRECTIONS:
            obstacle = getattr(self, direction)
            if obstacle.passable:
                passable_directions.append(direction)
        return passable_directions

    def get_list_repr(self):
        if self.north.passable:
            row_1 = ['X', 'X', ' ', ' ',  'X', 'X']
        else:
            row_1 = ['X'] * 6

        row_2 = []
        row_3 = []
        row_4 = []
        if self.west.passable:
            row_2.append('X')
            row_3.append(' ')
            row_4.append('X')
        else:
            row_2.append('X')
            row_3.append('X')
            row_4.append('X')
        row_2.extend([' '] * 4)
        row_3.extend([' '] * 4)
        row_4.extend([' '] * 4)
        if self.east.passable:
            row_2.append('X')
            row_3.append(' ')
            row_4.append('X')
        else:
            row_2.append('X')
            row_3.append('X')
            row_4.append('X')

        if self.south.passable:
            row_5 = ['X', 'X', ' ', ' ',  'X', 'X']
        else:
            row_5 = ['X'] * 6

        return [row_1, row_2, row_3, row_4, row_5]

    def __str__(self):
        list_repr = self.get_list_repr()
        str_rows = []
        for row in list_repr:
            str_rows.append((''.join(row) + '\n'))
        return ''.join(str_rows)


class Maze:

    def __init__(self):
        self.rooms = {}

    def add_room(self, coords, room):
        self.rooms[coords] = room

    def get_room_coords(self, room):
        if room in self.rooms.values():
            return list(filter(lambda x: x[1] == room, self.rooms.items()))[0][0]
        else:
            return None

    def get_door_directions_from_coords(self, coords_1, coords_2):
        x1, y1 = coords_1
        x2, y2 = coords_2
        x_delta = x1 - x2
        y_delta = y1 - y2
        if x_delta == 0:
            if y_delta > 0:
                return 'west', 'east'
            else:
                return 'east', 'west'
        elif x_delta > 0:
            return 'south', 'north'
        else:
            return 'north', 'south'

    def add_door_with_coords(self, room_1_coords, room_2_coords):
        room_1 = self.rooms[room_1_coords]
        room_2 = self.rooms[room_2_coords]
        door = Door((room_1, room_2))
        door_direction_room_1, door_direction_room_2 = self.get_door_directions_from_coords(
            room_1_coords,
            room_2_coords,
        )
        room_1.set_direction(door_direction_room_1, door)
        room_2.set_direction(door_direction_room_2, door)

    @staticmethod
    def get_neighbors_possible_coords(coords):
        x, y = coords
        possible_coords = (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
        return possible_coords

    def get_neighbors(self, coords):
        possible_coords = self.get_neighbors_possible_coords(coords)
        neighbors = []
        for some_coords in possible_coords:
            try:
                room = self.rooms[some_coords]
            except KeyError:
                pass
            else:
                neighbors.append(room)
        return neighbors

    def get_list_representation(self):
        x_coords = [x for x, y in self.rooms.keys()]
        y_coords = [y for x, y in self.rooms.keys()]
        min_x = min(x_coords)
        min_y = min(y_coords)
        max_x = max(x_coords)
        max_y = max(y_coords)
        empty_room_representation = [[' '] * 3] * 3
        final_list = []
        for x in range(min_x, max_x + 1):
            room_row = []
            for y in range(min_y, max_y + 1):
                try:
                    room = self.rooms[(x, y)]
                except KeyError:
                    room_representation = empty_room_representation
                else:
                    room_representation = room.get_list_repr()
                room_row.append(room_representation)
            final_list.append(room_row)
        return final_list

    def __str__(self):
        list_representation = self.get_list_representation()
        final_rows = []
        for row in list_representation:
            converted_rows = list(starmap(add_m, zip(*row)))
            converted_rows.reverse()
            final_rows.extend(converted_rows)
        str_rows = []
        for row in final_rows:
            str_row = ''.join(row) + '\n'
            str_rows.append(str_row)
        str_rows.reverse()
        return ''.join(str_rows)


class VisitedRoomsTracker:

    def __init__(self, maze_size):
        self.visited = {}
        self.maze_size = maze_size
        self.current_location = None

    def initialize(self):
        for x in range(self.maze_size):
            for y in range(self.maze_size):
                self.visited[(x, y)] = False

        self.current_location = (0, 0)

    def mark_visited(self, coords):
        self.visited[coords] = True

    def set_current_location(self, coords):
        self.current_location = coords

    def get_unvisited_neighbors(self):
        possible_neighbors = Maze.get_neighbors_possible_coords(self.current_location)
        not_visited_neighbors = []
        for neighbor_coords in possible_neighbors:
            try:
                visited = self.visited[neighbor_coords]
            except KeyError:
                continue
            else:
                if visited is False:
                    not_visited_neighbors.append(neighbor_coords)
        return not_visited_neighbors


class SquareMazeCreator:

    def __init__(self, maze_size):
        self.maze = Maze()
        self.maze_size = maze_size
        self.visited_tracker = VisitedRoomsTracker(maze_size)

    def init_maze(self):
        for x in range(self.maze_size):
            for y in range(self.maze_size):
                room = Room.create_with_walls()
                self.maze.add_room((x, y), room)

    def generate_maze(self):
        self.init_maze()
        self.visited_tracker.initialize()

        stack = [self.visited_tracker.current_location]
        self.visited_tracker.mark_visited(self.visited_tracker.current_location)
        while stack:
            coords = stack.pop()
            self.visited_tracker.set_current_location(coords)
            unvisited = self.visited_tracker.get_unvisited_neighbors()
            if unvisited:
                stack.append(coords)
                next_coords = random.choice(unvisited)
                self.maze.add_door_with_coords(coords, next_coords)
                self.visited_tracker.mark_visited(next_coords)
                stack.append(next_coords)

        return self.maze










