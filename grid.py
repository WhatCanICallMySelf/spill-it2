from cell import Cell

class Grid:
    def __init__(self, size: int):
        self._size = size

        # Create square 2d array of cells
        self._grid = [[Cell() for _ in range(size)] for _ in range(size)]

    def __str__(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self._grid)

    def get_cell(self, x, y):
        if x < 0 or y < 0 or x >= len(self._grid) or y >= len(self._grid[x]):
            return None
        return self._grid[x][y]
    