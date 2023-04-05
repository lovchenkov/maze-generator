from maze import Maze
from algorithms import build_maze_with_mst
import sys
from algorithms import build_maze_with_dfs
#import pygame

gen_algorithm = sys.argv[1]
height = int(sys.argv[2])
width = int(sys.argv[3])

maze = Maze(height, width)
if gen_algorithm == 'mst':
    build_maze_with_mst(maze)
else:
    build_maze_with_dfs(maze)
maze.find_path()
maze.visualize()