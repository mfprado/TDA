class Board:
    def __init__(self):
        self.cells = []
        self.ships = []

    def addCell(self, cell):
        self.cells += [cell]

    def addShip(self, ship):
        self.ships += [ship]

    def shipAlive(self):
        for ship in self.ships:
            if ship.alive():
                return True
        return False
