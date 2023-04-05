from maze import Maze
import random
from constants import directions


def random_starting_cell(maze: Maze) -> tuple:
    return 0, random.randint(0, maze.width - 1)


def random_ending_cell(maze: Maze) -> tuple:
    return maze.height - 1, random.randint(0, maze.width - 1)


def build_maze_with_dfs(maze: Maze) -> None:
    maze.starting_cell = random_starting_cell(maze)
    maze.ending_cell = random_ending_cell(maze)
    visited = dict()
    stack = [maze.starting_cell]
    while stack:
        current_cell = stack.pop()
        visited[current_cell] = True
        neighbour_directions = directions
        random.shuffle(neighbour_directions)
        for direction in neighbour_directions:
            neighbour_cell = maze.get_neighbour_cell(current_cell, direction)
            if neighbour_cell != (-1, -1) and not visited.get(neighbour_cell, False):
                maze.break_border(current_cell, neighbour_cell, direction)
                stack.append(neighbour_cell)
                visited[neighbour_cell] = True
    maze.grid[maze.starting_cell]['N'] = False
    maze.grid[maze.ending_cell]['S'] = False


def build_maze_with_mst(maze: Maze) -> None:
    max_weight = 100
    maze.starting_cell = random_starting_cell(maze)
    maze.ending_cell = random_ending_cell(maze)
    edges = []
    for i in range(maze.height):
        for j in range(maze.width):
            if i < maze.height - 1:
                edges.append([random.randint(0, max_weight), (i, j), (i + 1, j), 'S'])
            if j < maze.width - 1:
                edges.append([random.randint(0, max_weight), (i, j), (i, j + 1), 'E'])
    current_st = [maze.starting_cell]
    current_st_edges = []
    while len(current_st) != maze.grid_size:
        min_edge = [max_weight + 1, 0, 0, '#']
        for edge in edges:
            if (edge[1] in current_st) != (edge[2] in current_st):
                min_edge = min(min_edge, edge)
        new_cell = min_edge[1] if min_edge[2] in current_st else min_edge[2]
        current_st.append(new_cell)
        current_st_edges.append(min_edge)
    for edge in current_st_edges:
        maze.break_border(edge[1], edge[2], edge[3])

    maze.grid[maze.starting_cell]['N'] = False
    maze.grid[maze.ending_cell]['S'] = False



