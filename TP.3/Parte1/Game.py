import csv
from Board import *
from Cell import *


class Game:

    def __init__(self, path, strategy, shuttles):

        self.strategy = strategy
        self.shuttles = shuttles
        self.initializeBoard(path)

    def initializeBoard(self, path):
        file = open(path, 'r')
        reader = csv.reader(file, delimiter=' ')
        rows = sum(1 for row in file)
        file.seek(0)
        columns = len(next(reader)) - 1
        file.seek(0)

        self.board = Board(rows)
        actualRow = 0
        for line in reader:
            for i in range(1, columns + 1, 1):
                self.board.addCell(Cell(actualRow, i - 1, line[i]))
            self.board.addShip(line[0], actualRow)
            actualRow += 1


    def finished(self):
        return self.board.shipAlive()

    # def playTurn(self):




game = Game("board.csv", 1, 1)


