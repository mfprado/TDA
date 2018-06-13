class ShuttleArmor:
    def __init__(self, shuttlesCount):
        self.DAMAGE = 30
        self.shuttlesCount = shuttlesCount

    def attack(self, board):
        for cell in self.defineAttackCell(board):
            cell.getShip().receiveAttack(self.DAMAGE)
        board.removeDeadShip()

    def orderByDamage(self, cells):
    #     TODO
        return cells

    def defineAttackCells(self, board):
        candidateCells = board.getCellsWithShip()
        return self.orderByDamage(candidateCells)[0:self.shuttlesCount]
