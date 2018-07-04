from AttackStrategy import *
from itertools import permutations


class DinamicAttack(AttackStrategy):

    def __init__(self, shuttlesCount):
        AttackStrategy.__init__(self, shuttlesCount)
        self.deathShipsOrderToDie = None


    def attack(self, board):
        if self.deathShipsOrderToDie == None:
            self.defineShipsOrderToDie(board)
            self.attack(board)
        else:
            row = self.deathShipsOrderToDie[0]
            column = board.shipsActualColumn
            print("Ataque a celda (" + str(row) + " ," + str(column) + ") con las " + str(self.shuttlesCount) + " lanzaderas\n")
            for i in range(0, self.shuttlesCount):
                cellToAttack = board.cells[row][column]
                ship = cellToAttack.getShip()
                ship.receiveAttack(cellToAttack.damage)
                if not ship.alive():
                    i = self.shuttlesCount
                    if len(self.deathShipsOrderToDie) > 1:
                        self.deathShipsOrderToDie = self.deathShipsOrderToDie[1: len(self.deathShipsOrderToDie)]


    def defineShipsOrderToDie(self, board):
        deathOrderCombinations = list(permutations(range(0, board.rows)))
        for deathOrder in deathOrderCombinations:
            points = 0
            startColumn = 0
            for i in range(0, len(deathOrder)):
                shipRow = deathOrder[i]
                turnsCount = self.turnsToDieShipStartingInColumn(shipRow, startColumn)
                points += (len(deathOrder) - i) * turnsCount - 1
                startColumn += turnsCount%3

    def turnsToDieShipStartingInColumn(self, shipRow, startColumn):
        pass



