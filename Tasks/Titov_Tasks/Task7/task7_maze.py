import random


class Square:
    def __init__(self, x):
        self.__x = x
        self.__y = x

    def area(self):
        return self.__x * self.__y

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x


class Room:
    def __init__(self, count):
        self.__count = count

    def get_count(self):
        return self.__count


class Maze:

    def __init__(self):
        self.__rooms = {}
        self.numb = random.choice(range(1, square.area()))
        self.visited_list = [self.numb]

    def create_maze(self):
        count = 0
        next_visit = random.choice(
            self.search_neighbors(self.visited_list[-1]))
        if next_visit not in self.visited_list:
            count += 1
        self.visited_list.append(next_visit)
        if ('room', self.numb) in self.__rooms:
            if not ('room', next_visit) in self.__rooms[('room', self.numb)]:
                self.update_room(self.numb, next_visit)
                if ('room', next_visit) in self.__rooms:
                    if not self.numb in self.__rooms[('room', next_visit)]:
                        self.update_room(next_visit, self.numb)
                else:
                    self.add_room(next_visit, self.numb)
        else:
            self.add_room(self.numb, next_visit)
            self.add_room(next_visit, self.numb)
        self.numb = next_visit
        return count

    def search_neighbors(self, current_cell):
        neighbors = []
        if current_cell + square.get_y() < square.area():
            neighbors.append(current_cell + square.get_y())
        if current_cell - square.get_y() > 0:
            neighbors.append(current_cell - square.get_y())
        if current_cell % square.get_x() != 0:
            neighbors.append(current_cell + 1)
        if current_cell % square.get_x() != 1:
            neighbors.append(current_cell - 1)
        neighbors = self.del_replays_neighbors(neighbors)
        return neighbors

    def del_replays_neighbors(self, neighbors_list):
        valid_neighbors = []
        for neighbor in neighbors_list:
            if len(self.visited_list) > 1:
                if neighbor != self.visited_list[-2]:
                    valid_neighbors.append(neighbor)
            else:
                valid_neighbors.append(neighbor)
        return valid_neighbors

    def add_room(self, numb, next_visit):
        self.__rooms[('room', numb)] = [('room', next_visit)]

    def update_room(self, numb, next_visit):
        self.__rooms[('room', numb)].append(('room', next_visit))

    def print_maze(self):
        for k, v in self.__rooms.items():
            print(k, v, sep=": ")

    def get_rooms(self):
        return self.__rooms


count_room = 1

square = Square(5)
room = Room(20)
maze1 = Maze()

while count_room < room.get_count():
    count_room += maze1.create_maze()

if __name__ == "__main__":
    print("Maze path:", maze1.visited_list)
    print("Room exits:")
    maze1.print_maze()
