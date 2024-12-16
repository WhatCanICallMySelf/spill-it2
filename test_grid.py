from cell import Cell
from grid import Grid


def test_initialization():
    size = 3
    grid = Grid(size)

    # Check grid size
    assert len(grid._grid) == size
    assert all(len(row) == size for row in grid._grid)

    # Ensure all cells are instances of Cell
    for row in grid._grid:
        for cell in row:
            assert isinstance(cell, Cell)


def test_get_cell_with_valid_coordinates():
    size = 3
    grid = Grid(size)

    cell = grid.get_cell(1, 2)
    assert isinstance(cell, Cell)


def test_get_cell_with_invalid_coordinates():
    size = 3
    grid = Grid(size)

    assert grid.get_cell(-1, 0) is None
    assert grid.get_cell(0, -1) is None
    assert grid.get_cell(3, 0) is None
    assert grid.get_cell(0, 3) is None


def test_str_representation():
    grid = Grid(3)
    expected_output = (
        "2 [ ] [ ] [ ]\n"
        "1 [ ] [ ] [ ]\n"
        "0 [ ] [ ] [ ]\n"
        "   0   1   2"
    )
    assert str(grid) == expected_output
