from Ship import *


class Board:
    def __init__(self, rows):
        self.ships = []
        self.cells = []
        for row in range(0, rows, 1):
            self.cells.append([])

    def addCell(self, cell):
        self.cells[cell.row].append(cell)

    def addShip(self, shipLife, row):
        ship = Ship(shipLife, row, 0)
        self.ships.append(ship)
        self.cells[row][0].setShip(ship)

    def shipAlive(self):
        for ship in self.ships:
            if ship.alive():
                return True
        return False

    def moveShip(self):
        for ship in self.ships:
            (row, column) = ship.pos()
            self.cells[row, column].noShip()
            self.cells[row, column + 1].setShip(ship)
