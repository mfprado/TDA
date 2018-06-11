import sys
import Game


if __name__ == '__main__':
    board = sys.argv[1]
    strategy = sys.argv[2]
    SHUTTLES = sys.argv[3]
    game = Game("board.csv", 1, 1)
    # game = Game(board,strategy, SHUTTLES)
    playerA = 0
    playerB = 0
    turn = 1
    while not game.finished():
        print "TURNO NÚMERO: " + turn
        (pointsA, pointsB) = game.playTurn()
        playerA += pointsA
        playerB += pointsB
        print "PUNTOS JUGADOR A: " + playerA
        print "PUNTOS JUGADOR B: " + playerB
        print "TURNOS TOTALES: " + turn
        turn += 1




