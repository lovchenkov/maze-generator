from src.maze import Maze
from src.constants import *
import pygame

pygame.init()
screen = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])


def draw_cell(edges: dict, coord: tuple, edge_length: float, EPSILON : float) -> None:
    if edges['N']:
        pygame.draw.rect(screen, MAZE_COLOR, (coord[0] - EPSILON, coord[1] - EPSILON, edge_length + 2 * EPSILON,
                                              edge_length * BORDER_THICK + 2 * EPSILON))
    if edges['S']:
        pygame.draw.rect(screen, MAZE_COLOR, (coord[0] - EPSILON, coord[1] + edge_length * (1 - BORDER_THICK) - EPSILON,
                         edge_length + 2 * EPSILON, edge_length * BORDER_THICK + 2 * EPSILON))
    if edges['W']:
        pygame.draw.rect(screen, MAZE_COLOR, (coord[0] - EPSILON, coord[1] - EPSILON,
                                              edge_length * BORDER_THICK + 2 * EPSILON, edge_length + 2 * EPSILON))
    if edges['E']:
        pygame.draw.rect(screen, MAZE_COLOR, (coord[0] + edge_length * (1 - BORDER_THICK) - EPSILON, coord[1] - EPSILON,
                         edge_length * BORDER_THICK + 2 * EPSILON, edge_length + 2 * EPSILON))


def draw_player(maze: Maze):
    edge_length = maze.edge_length
    pygame.draw.circle(screen, PLAYER_COLOR, (MAZE_LEFT_CORNER[0] + maze.player.coord[1] * edge_length + edge_length / 2,
                                              MAZE_LEFT_CORNER[1] + maze.player.coord[0] * edge_length + edge_length / 2),
                       edge_length / 3.4)


def draw_maze(maze: Maze) -> None:
    edge_length = maze.edge_length
    for cell in maze.grid.keys():
        cell = cell[1], cell[0]
        draw_cell(maze.grid[cell], (MAZE_LEFT_CORNER[0] + edge_length * cell[1],
                  MAZE_LEFT_CORNER[1] + edge_length * cell[0]), edge_length, maze.EPSILON)
    draw_player(maze)


def draw_cell_in_path(maze: Maze, cell_index: int) -> None:
    current_cell = maze.path[cell_index]
    edge_length = maze.edge_length
    pygame.draw.rect(screen, PATH_COLOR,
                     (MAZE_LEFT_CORNER[0] + current_cell[1] * edge_length + edge_length * BORDER_THICK,
                     MAZE_LEFT_CORNER[1] + current_cell[0] * edge_length + edge_length * BORDER_THICK,
                     edge_length * (1 - 2 * BORDER_THICK) - 2 * maze.EPSILON,
                     edge_length * (1 - 2 * BORDER_THICK) - 2 * maze.EPSILON))
    if cell_index == maze.current_cell_in_path - 1:
        return


def draw_path(maze: Maze) -> None:
    for i in range(maze.current_cell_in_path):
        draw_cell_in_path(maze, i)
    if maze.current_cell_in_path != len(maze.path):
        maze.current_cell_in_path += 1




