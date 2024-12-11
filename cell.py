#defines class cell
class Cell:
    """
Definerer klassen cell

self._neighbour = int
    Teller hvor mange bomber det er rundt cellen

self._has_bomb = boolean
    Ser om den aktuelle cellen er en bombe

self._flagged = boolean
    Markerer at en celle er en bombe, uten å åpne den

set_bomb
"""

    def __init__(self):
        self._neighbour_bombs = 0
        self._has_bomb = False
        self._flagged = False

# self string for objects in class Cell
    def __str__(self):
        if self._flagged:
            return "[f]"
        return f"[{self._neighbour_bombs}]"
        
# Turns a cell into a bomb        
    def set_bomb(self, bool):
        self._has_bomb = bool

# Marks that a cell is flagged
    def set_flag(self, bool):
        self._flagged = bool 

# Returnerer verdien til self._has_bomb
    def has_bomb(self):
        return self._has_bomb
        
# Returnerer verdien til self._flagged
    def has_flag(self):
        return self._flagged
    
# Returnerer hvor mange av de omringende cellene som er bomber
    def neighbours(self):
        return self._neighbour_bombs
