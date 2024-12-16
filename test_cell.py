from cell import Cell


def test_initial_state():
    cell = Cell()
    assert not cell.has_bomb
    assert not cell.has_flag
    assert not cell.is_cleared
    assert cell.neighbor_bombs == 0


def test_set_bomb():
    cell = Cell()
    cell.set_bomb(True)
    assert cell.has_bomb

    cell.set_bomb(False)
    assert not cell.has_bomb


def test_set_flag():
    cell = Cell()
    cell.set_flag(True)
    assert cell.has_flag

    cell.set_flag(False)
    assert not cell.has_flag


def test_set_cleared():
    cell = Cell()
    cell.set_cleared(True)
    assert cell.is_cleared

    cell.set_cleared(False)
    assert not cell.is_cleared


def test_set_neighbor_bombs():
    cell = Cell()
    cell.set_neighbor_bombs(3)
    assert cell.neighbor_bombs == 3

    cell.set_neighbor_bombs(0)
    assert cell.neighbor_bombs == 0


def test_str_representation():
    cell = Cell()

    # Test initial state (not cleared, no flags, no bombs)
    assert str(cell) == "[ ]"

    # Test flag state
    cell.set_flag(True)
    assert str(cell) == "[f]"
    cell.set_flag(False)

    # Test cleared state
    cell.set_cleared(True)
    cell.set_neighbor_bombs(8)
    assert str(cell) == "[8]"
