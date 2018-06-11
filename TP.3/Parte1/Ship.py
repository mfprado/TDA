class Ship:

    def __init__(self, life, row, column):
        self.life = life
        self.row = row
        self.column = column

    def alive(self):
        return self.life > 0

    def pos(self):
        return self.row, self.column

    def receiveAttack(self, damage):
        self.life -= damage