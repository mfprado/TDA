import sys
import Game


if __name__ == '__main__':
    boardPath = sys.argv[1]
    strategy = sys.argv[2]
    shuttlesCount = sys.argv[3]
    game = Game("board.csv", 1, 1)
    # game = Game(boardPath, strategy, shuttlesCount)
    playerA = 0
    playerB = 0
    turn = 1
    while not game.finished():
        print "TURNO NÚMERO: " + turn
        # game.board draw TODO
        (pointsA, pointsB) = game.playTurn()
        # game.board draw TODO
        playerA += pointsA
        playerB += pointsB
        print "PUNTOS JUGADOR A: " + playerA
        print "PUNTOS JUGADOR B: " + playerB
        print "TURNOS TOTALES: " + turn
        turn += 1




