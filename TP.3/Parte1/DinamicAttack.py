from AttackStrategy import *
from itertools import permutations



class DinamicAttack(AttackStrategy):

    def __init__(self, shuttlesCount):
        AttackStrategy.__init__(self, shuttlesCount)
        self.deathShipsOrder = [0,1,2]


    def attack(self, board):
        if self.deathShipsOrder == None:
            self.defineAttacksByTurn(board)
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


    def defineAttacksByTurn(self, board):
        deathOrderCombinations = list(permutations(range(0, board.rows)))
        # for deathOrder in deathOrderCombinations:
        #     points = 0
        #     startColumn = 0
        #     for i in range(0, len(deathOrder)):
        #         shipRow = deathOrder[i]
        #         turnsCount = turnsToDieShipStartingInColumn(shipRow, startColumn)
        #         points += (len(deathOrder) - i) * turnsCount - 1
        #         startColumn += turnsCount%3



