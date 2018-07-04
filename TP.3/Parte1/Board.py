from Ship import *


class Board:
    def __init__(self, rows):
        self.shipsActualColumn = 0
        self.cells = []
        for row in range(0, rows, 1):
            self.cells.append([])
        self.rows = rows


    def addCell(self, cell):
        self.cells[cell.row].append(cell)

    def addShip(self, shipLife, row):
        ship = Ship(shipLife)
        self.cells[row][0].setShip(ship)

    def getCellsWithShip(self):
        cells = []
        for row in self.cells:
            cell = row[self.shipsActualColumn]
            if cell.getShip() is not None:
                cells.append(cell)
        return cells

    def getShips(self):
        ships = []
        for cell in self.getCellsWithShip():
            ships.append(cell.getShip())
        return ships

    def shipAlive(self):
        return len(self.getShips()) > 0

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
            cell = row[previousColumn]
            if cell.getShip() is not None and cell.getShip().alive():
                ship = cell.getShip()
                row[previousColumn].noShip()
                row[self.shipsActualColumn].setShip(ship)

    def shipsAliveCount(self):
        return len(self.getShips())

    def removeDeadShips(self):
        for cell in self.getCellsWithShip():
            if not cell.shipAlive():
                cell.noShip()

    def draw(self):
        draw = ""
        for row in self.cells:
            for i in range(0, len(row)):
                draw += " _____ "
            draw += ("\n")
            for cell in row:
                draw += "|"
                if not cell.ship == None:
                    draw += "\033[94mBARCO\033[0m"
                else:
                    draw += "     "
                draw += "|"
            draw += "\n"
            for cell in row:
                draw += "|"
                point = ""
                if not cell.ship == None:
                    point += "V:" + str(cell.getShip().life)
                else:
                    point += "     "
                if len(point) < 5:
                    for i in range(0, 5 - len(point)):
                        point += " "
                draw += "\033[93m" + point + "\033[0m|"
            draw += "\n"
            for cell in row:
                draw += "|"
                cellDamage = "D:" + str(cell.damage)
                if len(cellDamage) < 5:
                    for i in range(0, 5 - len(cellDamage)):
                        cellDamage += " "
                draw += "\033[91m" + cellDamage + "\033[0m|"
            draw += "\n"
            for i in range(0, len(row)):
                draw += " ----- "
            draw += ("\n")
        print(draw)
