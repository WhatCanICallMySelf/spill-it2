#defines class cell
class Cell:
    def __init__(self):
        self._neighbour_bombs = 0
        self._has_bomb = False
        self._flagged = False

# self string for objects in class Cell
    def __str__(self):
        if self._has_bomb:
            return f"This cell is a bomb. It has {self._neighbour_bombs} surronding bombs"
        else:
            return f"This cell is not a bomb. It has {self._neighbour_bombs} surronding bombs"
        
# Turns a cell into a bomb        
    def set_bomb(self, bool):
        self._has_bomb = bool

# Marks that a cell is flagged
    def set_flag(self, bool):
        self._flagged = bool