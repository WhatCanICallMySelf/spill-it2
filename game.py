from grid import Grid

GRID_SIZE = 10


    # Game class needs four functions to 
        # place the bombs on grid: grid.place_bombs()
        # draw the board with the correct cells: grid.show()
        # check if you have won: grid.victory()
        # open a cell and expand the cells without neighbours: grid.open()
        # cell should have boolean for revealed and not revealed cell.revealed()

    # TODO:
    # lag en function help som skriver ut regler for spillet og lovlige kommandoer
    # legg til en ny kommando q for quit
    # bytte om slik at alle komentarer og printer er på engelsk
    # senere:
    # inne i open comandoen må jeg sjekke om cellen allerede er revealed etter at det har blitt lagt inn en funksjon for det i cell.py
    # start timer når man gjør game start 
    # vise hvor mye tid per trekk og når man er ferdig med runden   


class Game: 
    def __init__(self):
        self._grid = Grid(GRID_SIZE)
        self._alive = True

    def start(self):
        while self._alive:
            self.do_turn()
        print("GAME OVER")

    def restart(self):
        pass

    def do_turn(self): 
        print("-----------------------------------------------")
        print("enter comand and cell coordinates. comands: o-open, f-flag, r-remove flag. example: f 4 6")
        # finnes ikke enda legg til når den blir laget i grid
        # self._grid.show()
        move_type = None
        x = None
        y = None
        try:
            move_type, x_str, y_str = input("input: ").split()
        except ValueError:
            print("feil format, prøv igjen")
            return
        
# testing: print(f"you typed: {move_type}, for the coordinates ({x}, {y})")
        
        try:
            x = int(x_str)
            y = int(y_str) 
        except ValueError:
            print("du må skrive to tall etter komandoen. foreksempel o 1 2 eller f 3 4")
            return
        # grid numbers are one lower in x and y 
        cell = self._grid.get_cell(x -1, y -1)

        if cell == None: 
            print(f"your coordinates are outside of the grid. choose a number 1-{GRID_SIZE}")
            return

        if move_type == "o": 
            print(f"opening cell {x}, {y}")
            # hadde vært fint å ha en function i cell for å sjekke has_bomb
            if cell.has_bomb == True:
                print("BOOOOOM")
                self._alive = False
            elif cell.has_flag == True:
                print(f"the coordinates you want to open is flagged. to clear this flag type c {x} {y}")
            else:
                # må legge til funksjon i cell for cell.open
                self._grid.open(x,y)
        elif move_type == "f": 
            print(f"placing a flagg at {x}, {y}")
            cell.set_flag(True)
        elif move_type == "r":
            print(f"removing a flagg at {x}, {y}")
            cell.set_flag(False)
        else: 
            print("feil komando, skriv o for åpne og f for flagg")
        
        # har vi vunnet nå?
        if self._grid.victory() == True:
            print("YOU WIN")
            self._alive = False

     

game = Game()
game.start()
