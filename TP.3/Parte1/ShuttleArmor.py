class ShuttleArmor:
    def __init__(self, shuttlesCount):
        self.shuttlesCount = shuttlesCount

    def orderByDamage(self, cells):
        cells.sort(key=lambda cell: cell.damage, reverse=True)
        return cells

    def defineCellsToAttack(self, board):
        return self.orderByDamage(board.getCellsWithShip())


    def attack(self, board):
        shoots = self.shuttlesCount
        for cell in self.defineCellsToAttack(board):
            if shoots <= 0:
                break
            ship = cell.getShip()
            while shoots > 0:
                    ship.receiveAttack(cell.damage)
                    shoots -= 1

