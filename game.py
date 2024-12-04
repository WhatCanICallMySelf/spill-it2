from grid import Grid

class Game: 
    def __init__(self):
        self._grid = Grid(10)

    def start(self):
        pass

    def restart(self):
        pass

    def gjør_trekk(self): 
        trekk = input("type the letter o to open or the letter f to flagg followed by the coordinates of the cell u want to interact with. eksempel: v 2 4")

        if len(trekk) < 3: 
            return ("det du skrev in følger ikke kravende prøv igjen")