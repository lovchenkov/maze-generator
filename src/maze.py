from constants import directions


class Maze(object):
    """
    keeps the maze and can be built with different parameters
    fields :
    int height
    int width
    dict grid -- keeps borders of each cell as a dict (N, S, W, E -> True, False)
    where True - there is a border of this direction, False - there isn't.
    int grid_size -- size of grid
    tuple starting_cell
    tuple  ending_cell
    list path -- path from starting to ending cell
    """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid_size = height * width
        self.grid = self._build_complete_grid()
        self.starting_cell = ()
        self.ending_cell = ()
        self.path = []

    def _build_complete_grid(self) -> dict:
        grid = dict()
        for i in range(self.height):
            for j in range(self.width):
                grid[(i, j)] = {'W': True, 'S': True, 'E': True, 'N': True}
        return grid

    def visualize(self) -> None:
        for i in range(2 * self.starting_cell[1] + 1):
            print('  ', end='')
        print('#')
        for i in range(2 * self.height + 1):
            for j in range(2 * self.width + 1):
                if i == 2 * self.height and j == 2 * self.width:
                    print('.', end=' ')
                    continue
                if i % 2 == 0:
                    if j % 2 == 0:
                        print('.', end=' ')
                    elif i == 2 * self.height:
                        if j % 2 == 0:
                            print('.', end=' ')
                        elif self.grid[(self.height - 1, j // 2)]['S']:
                            print('.', end=' ')
                        else:
                            print(' ', end=' ')

                    elif self.grid[(i // 2, j // 2)]['N']:
                        print('.', end=' ')
                    else:
                        print(' ', end=' ')
                else:
                    if j % 2 == 1:
                        if (i // 2, j // 2) in self.path:
                            print('#', end=' ')
                        else:
                            print(' ', end=' ')
                    elif j == 2 * self.width:
                        if self.grid[(i // 2, self.width - 1)]['E']:
                            print('.', end=' ')
                        else:
                            print(' ', end=' ')
                    elif self.grid[(i // 2, j // 2)]['W']:
                        print('.', end=' ')
                    else:
                        print(' ', end=' ')
            print()
        for i in range(2 * self.ending_cell[1] + 1):
            print('  ', end='')
        print('#')

    def break_border(self, cell1, cell2, relation: str) -> None:
        match relation:
            case 'N':
                self.grid[cell1]['N'] = False
                self.grid[cell2]['S'] = False
            case 'S':
                self.grid[cell1]['S'] = False
                self.grid[cell2]['N'] = False
            case 'W':
                self.grid[cell1]['W'] = False
                self.grid[cell2]['E'] = False
            case 'E':
                self.grid[cell1]['E'] = False
                self.grid[cell2]['W'] = False

    def get_neighbour_cell(self, cell, direction: str) -> tuple:
        match direction:
            case 'N':
                return (cell[0] - 1, cell[1]) if cell[0] - 1 >= 0 else (-1, -1)
            case 'S':
                return (cell[0] + 1, cell[1]) if cell[0] + 1 < self.height else (-1, -1)
            case 'W':
                return (cell[0], cell[1] - 1) if cell[1] - 1 >= 0 else (-1, -1)
            case 'E':
                return (cell[0], cell[1] + 1) if cell[1] + 1 < self.width else (-1, -1)

    def find_path(self):
        used = dict()
        parent = dict()
        stack = [self.starting_cell]
        used[self.starting_cell] = True
        parent[self.starting_cell] = (-1, -1)
        while stack:
            current_cell = stack.pop(0)
            for direction in directions:
                new_cell = self.get_neighbour_cell(current_cell, direction)
                if new_cell != (-1, -1) and not self.grid[current_cell][direction] and not used.get(new_cell, False):
                    stack.append(new_cell)
                    parent[new_cell] = current_cell
                    used[new_cell] = True
        path_end = self.ending_cell
        while path_end != (-1, -1):
            self.path.insert(0, path_end)
            path_end = parent[path_end]
