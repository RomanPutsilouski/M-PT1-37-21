import random
import networkx as nx
import matplotlib.pyplot as plt


class Room:
    def __init__(self, room_id, doors):
        self.room_id = room_id
        self.doors = doors


class Maze:
    def __init__(self, rooms):
        self.maze = {}
        self.maze_dict = {}
        self.rooms = rooms

    def maze_room_append(self, room):
        self.maze[room.room_id] = room

    def maze_dict_generate(self):
        listing = [x for x in range(1, self.rooms)]
        self.maze_dict = {x: [] for x in range(self.rooms)}

        for a in self.maze_dict:
            num = random.randint(1, 2)
            self.maze_dict[a] = listing[:num]
            listing = listing[num:]

        for k, v in self.maze_dict.items():
            for n, m in self.maze_dict.items():
                if k in m:
                    self.maze_dict[k] = [n] + v

        return self.maze_dict

    def maze_generate(self, maze_dict):
        for k, v in maze_dict.items():
            self.maze_room_append(Room(k, v))

    def create_maze(self):
        self.maze_generate(self.maze_dict_generate())


class Npc:
    def __init__(self, npc_type, current_maze, npc_position=None):
        self.npc_type = npc_type
        self.current_maze = current_maze
        self.npc_position = npc_position

    def move(self):
        self.npc_position = random.choice(self.current_maze.maze[self.npc_position].doors)
        print(f'{self.npc_type} переместился в комнату {self.npc_position}')
        return self.npc_position


class Play:
    def __init__(self, rooms):
        self.rooms = rooms

    def start(self):
        self.maze = Maze(self.rooms)
        self.maze.create_maze()
        hero = Npc('Супермен', self.maze, 0)
        print(f'{hero.npc_type} заспавнился в комнате {hero.npc_position}')
        monster = Npc('Годзила', self.maze, random.choice(list(self.maze.maze.keys())))
        print(f'{monster.npc_type} заспавнился в комнате {monster.npc_position}')
        cross = False
        while not cross:
            hero.move()
            if hero.npc_position != monster.npc_position:
                monster.move()
                if hero.npc_position == monster.npc_position:
                    cross = True
            else:
                cross = True

        print(f'{hero.npc_type} и {monster.npc_type} встретились в комнате {hero.npc_position}')


start = Play(10)
start.start()


graph = []
for i, v in start.maze.maze_dict.items():
    for a in v:
        graph.append((i, a))

G = nx.DiGraph()
G.add_nodes_from(start.maze.maze_dict.keys())
G.add_edges_from(graph)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()
