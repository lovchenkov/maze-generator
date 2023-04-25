import sys
import pygame
from src.maze import *
from src.algorithms import *
from src.display import *


class App(object):
    def __init__(self, new_screen):
        self.screen = new_screen
        self.screen = new_screen
        self.maze = Maze(1, 1)
        self.fps_clock = pygame.time.Clock()

    def initialize(self):
        height = int(sys.argv[1])
        gen_algorithm = sys.argv[2]

        width = height
        if gen_algorithm != 'mst' and gen_algorithm != 'dfs':
            raise Exception("Incorrect building_algorithm. Try 'dfs' or 'mst'.")
        if gen_algorithm == 'mst' and height > 25:
            raise Exception("Size is too big for mst, max value is 25.")
        if height < 5:
            raise Exception("Size it too small, you deserve more.")

        self.maze = Maze(height, width)
        if gen_algorithm == 'mst':
            build_maze_with_mst(self.maze)
        else:
            build_maze_with_dfs(self.maze)

        self.maze.set_player()

        self.maze.find_path()

        output = open("solution/solution.txt", 'w')
        sys.stdout = output
        self.maze.write_in_file()
        output.close()
        self.fps_clock.tick(FPS)

    def update_screen(self):
        self.screen.fill(SCREEN_COLOR)
        draw_maze(self.screen, self.maze)
        pygame.display.flip()
        self.fps_clock.tick(FPS)

    def update_path(self):
        self.screen.fill(SCREEN_COLOR)
        draw_maze(self.screen, self.maze)
        draw_path(self.screen, self.maze)
        pygame.display.flip()
        self.fps_clock.tick(10)

    def update_fps(self):
        if self.maze.grid_size <= 20:
            self.fps_clock.tick(10)
        elif self.maze.grid_size <= 80:
            self.fps_clock.tick(20)
        elif self.maze.grid_size <= 150:
            self.fps_clock.tick(60)
        elif self.maze.grid_size <= 300:
            self.fps_clock.tick(100)
        elif self.maze.grid_size <= 800:
            self.fps_clock.tick(200)
        elif self.maze.grid_size <= 2000:
            self.fps_clock.tick(400)
        elif self.maze.grid_size <= 5000:
            self.fps_clock.tick(600)
        elif self.maze.grid_size <= 15000:
            self.fps_clock.tick(800)

    def set_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("dist/Untilited.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def set_ryan_gosling(self):
        imp = pygame.image.load("dist/Untitled.png")
        self.screen.blit(imp, (WIDTH_SCREEN // 8, HEIGHT_SCREEN // 8))
        pygame.display.flip()
