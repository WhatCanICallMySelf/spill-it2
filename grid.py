from cell import Cell


class Grid:
    def __init__(self, size: int):
        """
        Initializes a Grid object with a specified size.

        :param size: The size (width and height) of the square grid.
        """
        self._size = size

        # Create square 2d array of size size with cells
        self._grid = [[Cell() for _ in range(size)] for _ in range(size)]

    def __str__(self) -> str:
        """
        Returns a string representation of the grid.
        """
        rows = "\n".join(
            f"{i} " + " ".join(str(cell) for cell in row) for i, row in reversed(list(enumerate(self._grid))))
        footer = "\n   " + "   ".join(str(i) for i in range(self._size))
        return rows + footer

    def get_cell(self, x: int, y: int) -> Cell | None:
        """
        Retrieves the Cell at the specified (x, y) coordinates.

        :param x: The x-coordinate (row index).
        :param y: The y-coordinate (column index).
        :return: The Cell object at (x, y) or None if the coordinates are out of bounds.
        """
        if x < 0 or y < 0 or x >= len(self._grid) or y >= len(self._grid[x]):
            return None
        return self._grid[y][x]
