from cell import Cell

def test_has_bomb():
    test = Cell()
    test.set_bomb(True)
    assert test.has_bomb() == True

def test_has_flag():
    flagtest = Cell()
    flagtest.set_flag(True)
    assert flagtest.has_flag() == True

def test_neighbours():
    celletest = Cell()
    assert celletest.neighbours() == 0

