from Ship import *


class Board:
    def __init__(self, rows):
        self.shipsActualColumn = 0
        self.cells = []
        for row in range(0, rows, 1):
            self.cells.append([])

    def addCell(self, cell):
        self.cells[cell.row].append(cell)

    def addShip(self, shipLife, row):
        ship = Ship(shipLife)
        self.cells[row][0].setShip(ship)

    def getShips(self):
        ships = []
        for row in self.cells:
            ships.append(row[self.shipsActualColumn].getShip())
        return ships

    def shipAlive(self):
        for ship in self.getShips():
            if ship.alive():
                return True
        return False

    def columnsCount(self):
        return len(self.cells[0])

    def updateShipsColumn(self):
        if self.shipsActualColumn == (self.columnsCount() - 1):
            self.shipsActualColumn = 0
        else:
            self.shipsActualColumn += 1

    def moveShips(self):
        previousColumn = self.shipsActualColumn
        self.updateShipsColumn()
        for row in self.cells:
            ship = row[previousColumn].getShip()
            row[previousColumn].noShip()
            row[self.shipsActualColumn].setShip(ship)


