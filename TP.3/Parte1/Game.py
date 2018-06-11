import csv
from Ship import *
from Board import *
from Cell import *


class Game:
    ROWS = 0
    COLUMNS = 0

    def __init__(self, path):
        file = open(path, 'r')
        reader = csv.reader(file, delimiter=' ')
        self.COLUMNS = len(next(reader)) - 1
        file.seek(0)

        self.board = Board()

        for line in reader:
            self.board.addShip(Ship(line[0]))
            for i in range(1, self.COLUMNS + 1, 1):
                self.board.addCell(Cell(self.ROWS, i-1, line[i]))
            self.ROWS += 1
        print 1


Game("board.csv")