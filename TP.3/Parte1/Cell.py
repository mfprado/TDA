class Cell:
    row = 0
    column = 0
    damage = 0
    ship = None

    def __init__(self, row, column, damage):
        self.row = row
        self.column = column
        self.damage = damage

    def noShip(self):
        self.ship = None

    def setShip(self, ship):
        self.ship = ship

    def getShip(self):
        return self.ship

    def shipAlive(self):
        if self.ship is not None:
            return self.ship.alive()
        return False