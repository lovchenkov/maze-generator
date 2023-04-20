

class Player(object):
    """
    keeps current cell that the player is on. We can move it in four
    directions.
    """
    def __init__(self, coord: tuple):
        self.coord = coord
        self.path = []

    def move(self, direction) -> None:
        match direction:
            case 'N':
                self.coord = (self.coord[0] - 1, self.coord[1])
            case 'S':
                self.coord = (self.coord[0] + 1, self.coord[1])
            case 'W':
                self.coord = (self.coord[0], self.coord[1] - 1)
            case 'E':
                self.coord = (self.coord[0], self.coord[1] + 1)



