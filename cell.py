#defines class cell
class Cell:
    def __init__(self):
        self._neighbour_bombs = 0
        self._has_bomb = False
        self._has_flag = False
        self._is_cleared = False

# self string for objects in class Cell
    def __str__(self):
        #if self._has_bomb:
        #    return "\033[41m[B]\033[0m"
        if self._is_cleared:
            return f"[{self._neighbour_bombs}]"
        if self._has_flag:
            return "[f]"
        return "[ ]"

    @property
    def has_bomb(self):
        return self._has_bomb

    @property
    def has_flag(self):
        return self._has_flag

    @property
    def is_cleared(self):
        return self._is_cleared

    @property
    def neighbor_bombs(self):
        return self._neighbour_bombs

        
# Turns a cell into a bomb        
    def set_bomb(self, bool):
        self._has_bomb = bool

# Marks that a cell is flagged
    def set_flag(self, bool):
        self._has_flag = bool

    def set_cleared(self, is_cleared: bool):
        self._is_cleared = is_cleared

    def set_neighbor_bombs(self, amount: int):
        self._neighbour_bombs = amount
