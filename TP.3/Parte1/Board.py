class Board:
    def __init__(self):
        self.cells = []
        self.ships = []

    def addCell(self, cell):
        self.cells += [cell]

    def addShip(self,ship):
        self.ships += [ship]