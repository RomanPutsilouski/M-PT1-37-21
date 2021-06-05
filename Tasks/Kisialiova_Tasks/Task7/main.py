from Tasks.Kisialiova_Tasks.Task7.characters import CharacterSpawner, CharacterInMazeProcessor
from maze import SquareMazeCreator

if __name__ == '__main__':
    maze_creator = SquareMazeCreator(maze_size=5)
    maze = maze_creator.generate_maze()
    print('Generated maze:')
    print(maze)

    characters = []
    character_spawner = CharacterSpawner(maze)
    hero = character_spawner.spawn_hero()
    monster = character_spawner.spawn_random_monster()
    characters_processor = CharacterInMazeProcessor([hero, monster])
    characters_processor.process_cycle()
