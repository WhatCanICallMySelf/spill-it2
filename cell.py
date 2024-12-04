#defines class cell
class Cell:
    def __init__(self, neighbour_bombs: int, has_bomb: bool, flagged: bool):
        self._neighbour_bombs = neighbour_bombs
        self._has_bomb = has_bomb
        self._flagged = flagged

# self string for objects in class Cell
    def __str__(self):
        if self._has_bomb:
            return f"This cell is a bomb. It has {self._neighbour_bombs} surronding bombs"
        else:
            return f"This cell is not a bomb. It has {self._neighbour_bombs} surronding bombs"
        
# Turns a cell into a bomb        
    def set_bomb(self):
        self._has_bomb = True

# Marks that a cell is flagged
    def set_flag(self):
        self._flagged = True
    
#Calculate how many surrounding neighbours the cell have
    def calculate_neighbour_bombs(self):
        self._neighbour_bombs = 0