from AttackStrategy import *

class GreedyAttack(AttackStrategy):

    def __init__(self, shuttlesCount, board):
        AttackStrategy.__init__(self, shuttlesCount, board)

    def orderByDamageFraction(self, cells):
        cells.sort(key=lambda cell: cell.damage/cell.getShip().life, reverse=True)
        for cell in cells:
            print("Celda: "+ "(" + str(cell.row) + ", " + str(cell.column) + ") " "Fraccion de danio: "+ str(cell.damage/cell.getShip().life))
        return cells

    def defineCellsToAttack(self, board):
        return self.orderByDamageFraction(board.getCellsWithShip())


    def attack(self, board):
        shoots = self.shuttlesCount
        print("Ataque a celdas: \n")
        for cell in self.defineCellsToAttack(board):
            if shoots <= 0:
                break
            ship = cell.getShip()
            while shoots > 0 and ship.alive():
                    print ("Lanzadera " + str(self.shuttlesCount - shoots) + ": " + "(" + str(cell.row) + ", " + str(cell.column) + ")")
                    ship.receiveAttack(cell.damage)
                    shoots -= 1
