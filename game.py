from grid import Grid

class Game: 
    def __init__(self):
        self._grid = Grid(10)
        self._alive = True

    def start(self):
        while self._alive:
            self.do_turn()


    def restart(self):
        pass

    def do_turn(self): 
        print("type the letter o to open or the letter f to flagg followed by the coordinates of the cell u want to interact with. example: v 2 4")
        # todo
        move_type, x, y = input("input: ")

game = Game()
Game.start()
