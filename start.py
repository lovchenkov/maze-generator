import sys
import pygame

height = int(sys.argv[1])
gen_algorithm = sys.argv[2]

width = height
if gen_algorithm != 'mst' and gen_algorithm != 'dfs':
    raise Exception("Incorrect building_algorithm. Try 'dfs' or 'mst'.")
if gen_algorithm == 'mst' and  height > 25:
    raise Exception("Size is too big for mst, max value is 30.")
if height < 5:
    raise Exception("Size it too small, you deserve more.")

from  src.algorithms import build_maze_with_mst
from src.algorithms import build_maze_with_dfs
from src.display import *
from src.constants import *

maze = Maze(height, width)
if gen_algorithm == 'mst':
    build_maze_with_mst(maze)
else:
    build_maze_with_dfs(maze)

maze.set_player()

maze.find_path()
output = open("solution/solution.txt", 'w')
sys.stdout = output
maze.write_in_file()
output.close()

screen.fill(SCREEN_COLOR)
draw_maze(maze)
pygame.display.flip()
fps = 10
fps_clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("dist/Untilited.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

# OPTIONS FOR STATUS ARE: PLAYING, SHOWING_PATH, FINISHED
STATUS = "PLAYING"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if maze.is_player_finished():
        STATUS = "FINISHED"
        imp = pygame.image.load("dist/Untitled.png")
        screen.blit(imp, (WIDTH_SCREEN // 8, HEIGHT_SCREEN // 8))
        pygame.display.flip()

    if STATUS != "FINISHED":
        pygame.mixer.music.pause()

    if STATUS == "FINISHED":
        pygame.mixer.music.unpause()
        continue

    if STATUS == "PLAYING":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            maze.move_player('S')
        if keys[pygame.K_UP]:
            maze.move_player('N')
        if keys[pygame.K_LEFT]:
            maze.move_player('W')
        if keys[pygame.K_RIGHT]:
            maze.move_player('E')
        if keys[pygame.K_TAB]:
            STATUS = "SHOWING_PATH"

        screen.fill(SCREEN_COLOR)
        draw_maze(maze)
        pygame.display.update()
        fps_clock.tick(fps)

    if STATUS == "SHOWING_PATH":
        if maze.grid_size <= 20:
            fps_clock.tick(10)
        elif maze.grid_size <= 80:
            fps_clock.tick(20)
        elif maze.grid_size <= 150:
            fps_clock.tick(60)
        elif maze.grid_size <= 300:
            fps_clock.tick(100)
        elif maze.grid_size <= 800:
            fps_clock.tick(200)
        elif maze.grid_size <= 2000:
            fps_clock.tick(400)
        elif maze.grid_size <= 5000:
            fps_clock.tick(600)
        elif maze.grid_size <= 15000:
            fps_clock.tick(1000)

        screen.fill(SCREEN_COLOR)
        draw_maze(maze)
        draw_path(maze)
        pygame.display.flip()
