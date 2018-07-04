from AttackStrategy import *
from itertools import permutations


class DinamicAttack(AttackStrategy):

    def __init__(self, shuttlesCount):
        AttackStrategy.__init__(self, shuttlesCount)
        self.deathShipsOrder = None
        self.turnsToKillShip = {}

    def attack(self, board):
        if self.deathShipsOrder == None:
            self.defineShipsOrderToDie(board)
            print(self.deathShipsOrder)
            self.attack(board)
        else:
            row = self.deathShipsOrder[0]
            column = board.shipsActualColumn
            print("Ataque a celda (" + str(row) + " ," + str(column) + ") con las " + str(self.shuttlesCount) + " lanzaderas\n")
            for i in range(0, self.shuttlesCount):
                cellToAttack = board.cells[row][column]
                ship = cellToAttack.getShip()
                ship.receiveAttack(cellToAttack.damage)
                if not ship.alive():
                    i = self.shuttlesCount
                    if len(self.deathShipsOrder) > 1:
                        self.deathShipsOrder = self.deathShipsOrder[1: len(self.deathShipsOrder)]

    def defineShipsOrderToDie(self, board):
        deathOrderCombinations = list(permutations(range(0, board.rows)))
        deathOrderCombinationsPoints = dict.fromkeys(deathOrderCombinations, 0)
        for deathOrder in deathOrderCombinations:
            points = 0
            startColumn = 0
            for i in range(0, len(deathOrder)):
                shipRow = deathOrder[i]
                turnsCount = self.turnsToKillShipStartingInColumn(shipRow, startColumn, board)
                points += (len(deathOrder) - i) * turnsCount - 1
                startColumn = (startColumn + turnsCount) % (board.rows-1)
            deathOrderCombinationsPoints[deathOrder] = points
        del self.turnsToKillShip
        self.deathShipsOrder = min(deathOrderCombinationsPoints, key=deathOrderCombinationsPoints.get)


    def turnsToKillShipStartingInColumn(self, shipRow, startColumn, board):
        if (shipRow, startColumn) in self.turnsToKillShip:
            return self.turnsToKillShip[(shipRow, startColumn)]
        else:
            turns = 0
            shipLife = board.cells[shipRow][0].getShip().life
            actualColumn = startColumn
            while shipLife > 0:
                shipLife -= self.shuttlesCount * board.cells[shipRow][actualColumn].damage
                turns += 1
                actualColumn = (actualColumn+1) % (board.rows-1)

            self.turnsToKillShip[(shipRow, startColumn)] = turns
            return turns



