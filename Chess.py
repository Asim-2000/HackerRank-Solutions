class ChessBoard:
    def __init__(self, board):
        self.board = [['o' for i in range(4)] for j in range(4)]
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.board[j][i] = board[j][i]

    def print_board(self):
        for y in range(3, -1, -1):
            print(self.board[y])


def get_queens(B):
    b = B.board
    WhiteQueen, BlackQueen = False, False
    for row in b:
        for t in row:
            if t == 'bQ':
                BlackQueen = True
            if t == 'wQ':
                WhiteQueen = True
    return WhiteQueen, BlackQueen


def get_boards2(B, player):
    board = B.board
    n = len(board)
    for row in range(n):
        for col in range(n):
            c, t = board[row][col]
            if c == player:
                for nBoard in get_boards(B, player, t, row, col):
                    yield nBoard


def get_boards(B, player, t, row, col):
    if t == 'Q':
        for deltaRow in [-1, 0, 1]:
            for deltaCol in [-1, 0, 1]:
                if deltaRow == 0 and deltaCol == 0:
                    continue
                for nb in borads_in_Straight_(B, player, t, row, col, deltaRow, deltaCol):
                    yield nb
    elif t == 'R':
        for deltaRow in [-1, 0, 1]:
            for deltaCol in [-1, 0, 1]:
                if (deltaRow == 0 and deltaCol == 0) or (deltaRow != 0 and deltaCol != 0):
                    continue
                for nb in borads_in_Straight_(B, player, t, row, col, deltaRow, deltaCol):
                    yield nb
    elif t == 'B':
        for deltaRow in [-1, 0, 1]:
            for deltaCol in [-1, 0, 1]:
                if deltaRow == 0 or deltaCol == 0:
                    continue
                for nb in borads_in_Straight_(B, player, t, row, col, deltaRow, deltaCol):
                    yield nb
    elif t == 'N':
        for nb in get_boards_moving_in_L_shape(B, player, t, row, col):
            yield nb


def borads_in_Straight_(B, player, t, row, col, deltaRow, deltaCol):
    step = 1
    while row + step*deltaRow >= 0 and row + step*deltaRow < 4 and col + step*deltaCol >= 0 and col + step*deltaCol < 4:
        c, _ = list(B.board[row+step*deltaRow][col+step*deltaCol])
        # print step,deltaRow,deltaCol,c,t
        if c == player:
            # blocked
            break
        # move
        nb = ChessBoard(B.board)
        nb.board[row+step*deltaRow][col+step*deltaCol] = player+t
        nb.board[row][col] = 'oo'

        yield nb
        if not c == player and c != 'o':
            # enemy piece
            break
        step += 1


def get_boards_moving_in_L_shape(B, player, t, row, col):
    deltas = [(-2, 1), (-1, 2), (1, 2), (2, 1),
              (2, -1), (1, -2), (-1, -2), (-2, -1)]
    for drow, dcol in deltas:
        if row + drow >= 0 and row + drow < 4 and col + dcol >= 0 and col + dcol < 4:
            c, _ = list(B.board[row+drow][col+dcol])
            if c == player:
                continue
            nb = ChessBoard(B.board)
            nb.board[row+drow][col+dcol] = player+t
            nb.board[row][col] = 'oo'
            yield nb


def WhiteWins(m, B, p, np):
    whiteQueen, blackQueen = get_queens(B)
    if not blackQueen and not whiteQueen:
        raise Exception('no queens')
    if not blackQueen:
       # if there is no black queen
        return True
    if not whiteQueen:
       # if there is no white queen
        return False
    # if there are 0 moves or if there is 1 move and p==numer of black pieces
    if m == 0 or (m == 1 and p == 'b'):
        return False

    if p == 'w':
        # white must win at leat one
        for nb in get_boards2(B, p):
            # nb.print_board()
            # print ''
            if WhiteWins(m-1, nb, np, p):
                return True
        return False

    # white must win all of them
    for nb in get_boards2(B, p):
        # nb.print_board()
        # print ''
        if not WhiteWins(m-1, nb, np, p):
            return False
    return True


def main():


    g = int(input())
    for j in range(g):
        w, b, m = list(map(int, input().split(' ')))
        board = [['oo' for x in range(4)] for y in range(4)]
        Columns = ['A', 'B', 'C', 'D']
        for i in range(w):
            t, c, r = input().split(' ')
            board[int(r)-1][Columns.index(c)] = 'w'+t
        for i in range(b):
            t, c, r = input().split(' ')
            board[int(r)-1][Columns.index(c)] = 'b'+t

        print('YES' if WhiteWins(m, ChessBoard(board), 'w', 'b') else 'NO')

if __name__ == '__main__':
    main()