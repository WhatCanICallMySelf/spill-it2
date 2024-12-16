import time
from random import randint

from grid import Grid

GRID_SIZE = 10
BOMB_COUNT = 20


# Game klassen håndterer hovedlogikken for spillet
# den starter spillet, håndterer spilleren sine trekk,
# oppretter bomber, oppdaterer rutenettet og sjekker om spillet er over

class Game:
    def __init__(self):
        self._grid = Grid(GRID_SIZE)
        self._alive = True
        self._generated_bombs = False
        self._start_time = time.time()
        self._cleared_cells = 0

    def play(self):
        while self._alive:
            self.do_turn()

    # Clear cell and expand cleared cells if cells have 0 bombs around them
    def clear_cell(self, cell, x: int, y: int):
        if cell.is_cleared:
            return

        cell.set_cleared(True)
        self._cleared_cells += 1

        # Check all neighbour cells in a 3x3 grid centred on cell being cleared
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                # If cell is current cell do nothing, prevents infinite recursion
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                neighbor = self._grid.get_cell(nx, ny)
                # Deals with "neighbours" outside the grid
                if neighbor is not None:
                    if not neighbor.has_bomb and cell.neighbor_bombs == 0:
                        self.clear_cell(neighbor, nx, ny)

    def randomize_bombs(self, bombs_to_place: int, safe_x: int, safe_y: int):
        # Places bombs randomly on the grid, except a 3x3 grid around the safe x and y
        if bombs_to_place >= GRID_SIZE ** 2:
            raise ValueError("Bombs to place must be less than amount of cells.")
        placed_bombs = 0
        while placed_bombs < bombs_to_place:
            x = randint(0, GRID_SIZE - 1)
            y = randint(0, GRID_SIZE - 1)
            # If x and y to place bomb is within safe 3x3 grid, do nothing
            if x in {safe_x, safe_x + 1, safe_x - 1} and y in {safe_y, safe_y + 1, safe_y - 1}:
                continue
            cell = self._grid.get_cell(x, y)
            if cell.has_bomb == True or cell.is_cleared == True:
                continue
            cell.set_bomb(True)
            placed_bombs += 1

    def set_neighbor_bombs(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = self._grid.get_cell(x, y)
                # Get 3x3 grid centered around current cell
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        # Ignore original cell
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        neighbor = self._grid.get_cell(nx, ny)
                        # Deals with "neighbours" outside the grid
                        if neighbor is not None:
                            if neighbor.has_bomb:
                                cell.set_neighbor_bombs(cell.neighbor_bombs + 1)

    # håndterer trekk som spilleren gjør
    def do_turn(self):
        print(self._grid)
        print("-----------------------------------------------")
        print("Type h for information on how to play the game")
        print("If you want to quit enter q")
        print("Type your move?")

        # finner total tiden på runden til spilleren
        current_time = time.time()
        print(f"Your time: {round(current_time - self._start_time, 1)}")

        command = input("input: ")
        if command[0] == "h":
            print("\n><><><><><><><><><><><><><><><><><><><")
            print("How to do type commands:")
            print(
                "comands: \no - open \nf - flag, \nr - remove flag \nEnter comand and cell coordinates. \nExample: f 4 6\n")
            print("how to play the game:")
            print(
                "Målet med spillet er å få vekk minene i et minefelt uten at de sprenger. \nDette kan man få til ved å se på tallene i minefeltet som viser hvor mange miner som er rundt denne ruten. \nMed denne informasjonen skal det være mulig å kunne unngå å sprenge minene.")
            print("><><><><><><><><><><><><><><><><><><><")

        elif command[0] == "q":
            print("You quit")
            self._alive = False

        else:
            # testing for feil formatering av input
            try:
                move_type, x_str, y_str = command.split()
            except ValueError:
                print("feil format, prøv igjen")
                return

            # testing for feil formatering av kordinater
            try:
                x = int(x_str)
                y = int(y_str)
            except ValueError:
                print("du må skrive to tall etter komandoen. foreksempel o 1 2 eller f 3 4")
                return
            cell = self._grid.get_cell(x, y)

            # sjekker om koordinatene er utenfor rutenetet
            if cell is None:
                print(f"your coordinates are outside of the grid. choose a number 0-{GRID_SIZE - 1}")
                return

            # gjør trekket utifra inputen
            if move_type == "o":
                # åpning av cellen
                print(f"opening cell {x}, {y}")
                # Generating bombs after first clear ensuring the first clear will expand bigger and not be a bomb
                if not self._generated_bombs:
                    self._generated_bombs = True
                    self.randomize_bombs(BOMB_COUNT, x, y)
                    self.set_neighbor_bombs()

                if cell.has_flag:
                    print(f"the coordinates you want to open is flagged. to clear this flag type r {x} {y}")

                elif cell.has_bomb:
                    print("BOOOOOM")
                    print("GAME OVER")
                    self._alive = False

                else:
                    self.clear_cell(cell, x, y)

                if self._cleared_cells == GRID_SIZE ** 2 - BOMB_COUNT:
                    print("YOU WIN")
                    self._alive = False

            elif move_type == "f":
                # plassering av flagg
                if cell.is_cleared:
                    print(f"the coordinates you want to flag is alredy open, so there is no need to flag this cell.")

                else:
                    print(f"placing a flag at {x}, {y}")
                    cell.set_flag(True)

            elif move_type == "r":
                # fjerning av flagg
                if cell.has_flag:
                    print(f"removing a flagg at {x}, {y}")
                    cell.set_flag(False)

                else:
                    print(f"the coordinates you want clear does not have a flag")

            else:
                print("feil komando, skriv o for åpne og f for flagg")


game = Game()
game.play()
