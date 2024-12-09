#defines class cell
class Cell:
    def __init__(self):
        self._neighbour_bombs = 0
        self._has_bomb = False
        self._has_flag = False
        self._is_cleared = False

# self string for objects in class Cell
    def __str__(self):
        if self._flagged:
            return "[f]"
        return f"[{self._neighbour_bombs}]"

    @property
    def has_bomb(self):
        return self._has_bomb

    @property
    def has_flag(self):
        return self._has_flag

    @property
    def is_cleared(self):
        return self._is_cleared

        
# Turns a cell into a bomb        
    def set_bomb(self, bool):
        self._has_bomb = bool

# Marks that a cell is flagged
    def set_flag(self, bool):
        self._has_flag = bool

    def set_cleared(self, is_cleared: bool):
        self._is_cleared = is_cleared

