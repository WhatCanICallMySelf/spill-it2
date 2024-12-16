from game import Game, GRID_SIZE
from grid import Grid


def test_initialization():
    game = Game()
    assert game._alive is True
    assert game._generated_bombs is False
    assert game._cleared_cells == 0
    assert isinstance(game._grid, Grid)


def test_randomize_bombs():
    game = Game()
    game.randomize_bombs(20, 5, 5)  # Replace with your own safe coordinates
    bombs_count = sum(cell.has_bomb for row in game._grid._grid for cell in row)
    assert bombs_count == 20


def test_set_neighbor_bombs():
    game = Game()
    game._grid.get_cell(0, 0).set_bomb(True)
    game._grid.get_cell(1, 1).set_bomb(True)
    game.set_neighbor_bombs()
    assert game._grid.get_cell(1, 0).neighbor_bombs == 2
    assert game._grid.get_cell(0, 1).neighbor_bombs == 2
    assert game._grid.get_cell(1, 2).neighbor_bombs == 1
    assert game._grid.get_cell(2, 1).neighbor_bombs == 1


def test_clear_cell():
    game = Game()
    game._grid.get_cell(0, 0).set_bomb(True)
    game.set_neighbor_bombs()

    cell = game._grid.get_cell(5, 5)
    game.clear_cell(cell, 5, 5)
    assert cell.is_cleared
    assert game._cleared_cells == (GRID_SIZE ** 2) - 1
