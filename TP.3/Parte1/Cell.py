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
        ship = None

    def setShip(self, ship):
        self.ship = ship
