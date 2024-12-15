from random import randint

from grid import Grid

import time


GRID_SIZE = 10
BOMB_COUNT = 20


    # Game class needs four functions to
        # check if you have won: grid.victory()
        # open a cell and expand the cells without neighbours: grid.open()

    # TODO:
    # senere:
    # inne i open comandoen må jeg sjekke om cellen allerede er revealed etter at det har blitt lagt inn en funksjon for det i cell.py
    # start timer når man gjør game start 
    # vise hvor mye tid per trekk og når man er ferdig med runden   


class Game:
    def __init__(self):
        self._grid = Grid(GRID_SIZE)
        self._alive = True
        self._generated_bombs = False
        self._start_time = time.time()
        self._cleared_cells = 0

    def start(self):
        while self._alive:
            self.do_turn()

    def clear_cell(self, cell, x:int, y:int):
        if cell.is_cleared:
            return

        cell.set_cleared(True)
        self._cleared_cells += 1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                neighbor = self._grid.get_cell(nx, ny)
                if neighbor is not None:
                    if not neighbor.has_bomb and cell.neighbor_bombs == 0:
                        self.clear_cell(neighbor, nx, ny)

    def randomize_bombs(self, bombs: int, safe_x, safe_y):
        if bombs >= GRID_SIZE**2:
            raise ValueError("Bombs must be less than amount of cells.")
        i = 0
        while i < bombs:
            x = randint(0, GRID_SIZE - 1)
            y = randint(0, GRID_SIZE - 1)
            if x in {safe_x, safe_x + 1, safe_x - 1} and y in {safe_y, safe_y + 1, safe_y - 1}:
                continue
            cell = self._grid.get_cell(x, y)
            if cell.has_bomb == True or cell.is_cleared == True:
                continue
            cell.set_bomb(True)
            i += 1

    def set_neighbor_bombs(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = self._grid.get_cell(x,y)
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        neighbor = self._grid.get_cell(nx, ny)
                        if neighbor is not None:
                            if neighbor.has_bomb == True:
                                cell.set_neighbor_bombs(cell.neighbor_bombs + 1)


    def do_turn(self): 
        print(self._grid)
        print("-----------------------------------------------")
        print("Type h for information on how to play the game")
        print("If you want to quit enter q")
        print("Type your move?")

        current_time = time.time()

        print(f"Your time: {round(current_time - self._start_time, 1)}")

        move_type = None
        x = None
        y = None
        command = input("input: ")
        if command[0] == "h":
            print("\n><><><><><><><><><><><><><><><><><><><")
            print("How to do type commands:")
            print("comands: \no - open \nf - flag, \nr - remove flag \nEnter comand and cell coordinates. \nExample: f 4 6\n")
            print("how to play the game:")
            print("Målet med spillet er å få vekk minene i et minefelt uten at de sprenger. \nDette kan man få til ved å se på tallene i minefeltet som viser hvor mange miner som er rundt denne ruten. \nMed denne informasjonen skal det være mulig å kunne unngå å sprenge minene.")
            print("><><><><><><><><><><><><><><><><><><><")


        elif command[0] == "q":
            print("You quit")
            self._alive = False
        else:

            try:
                move_type, x_str, y_str = command.split()
            except ValueError:
                print("feil format, prøv igjen")
                return
        
            try:
                x = int(x_str)
                y = int(y_str)
            except ValueError:
                print("du må skrive to tall etter komandoen. foreksempel o 1 2 eller f 3 4")
                return
            # grid numbers are one lower in x and y
            cell = self._grid.get_cell(x, y)

            if cell == None:
                print(f"your coordinates are outside of the grid. choose a number 0-{GRID_SIZE - 1}")
                return

            if move_type == "o":
                print(f"opening cell {x}, {y}")
                if not self._generated_bombs:
                    self._generated_bombs = True
                    self.randomize_bombs(BOMB_COUNT, x, y)
                    self.set_neighbor_bombs()

                if cell.has_flag == True:
                    print(f"the coordinates you want to open is flagged. to clear this flag type r {x} {y}")
                elif cell.has_bomb == True:
                    print("BOOOOOM")
                    print("GAME OVER")
                    self._alive = False
                else:
                    self.clear_cell(cell, x, y)
                    
                if self._cleared_cells == GRID_SIZE ** 2 - BOMB_COUNT:
                    print("YOU WIN")
                    self._alive = False
            elif move_type == "f":
                if cell._is_cleared == True:
                    print(f"the coordinates you want to flag is alredy open, so there is no need to flag this cell.")
                else:
                    print(f"placing a flag at {x}, {y}")
                    cell.set_flag(True)
            elif move_type == "r":
                if cell.has_flag == True:
                    print(f"removing a flagg at {x}, {y}")
                    cell.set_flag(False)
                else:
                    print(f"the coordinates you want clear does not have a flag")
            else:
                print("feil komando, skriv o for åpne og f for flagg")


     

game = Game()
game.start()
