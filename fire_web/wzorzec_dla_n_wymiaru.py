def pattern(n):
    board = []

    for x in range(0, n):
        board.append(["."] * n)

    def print_board(board):
        for row in board:  # każdy rząd jest oddzielną listą wewnątrz większej listy board
            print(" ".join(row))  # za każdym razem tworzy złączony rząd i powtarza tyle ile ich jest, czyli n = 5

    # board[row][col] = "X"  # odnosi się jeszcze do elemenów w dużej liscie (niezłączonej) - podgląd "print(board)"

    def raw_pattern(z):
        row_i = 1 # dla ramienia i (nie można dać wspólnych col i row dla obu ramion, bo po inkrementacji PRZED drugą pętlą col i row wynoszą już po 6)
        col_i = 1 # można też dać 2 i w górę ( w zależnosci od ), bo i tak jest możliwy ujemny/ odwrotny index w listach
        row_j = 1 # dla ramienia j
        col_j = 1
        for i in board:       # pierwsze ramię dla 5 podlist w całym board
            board[z-row_i][z-col_i] = "X"
            row_i +=1
            col_i +=1
        for j in board:       # drugie ramię
            board[z-row_j][col_j-1] = "X"     # rzędy się zmniejszają, kolumny rosną
            row_j += 1
            col_j += 1
        return print_board(board)

    #print(print_board(board))
    return raw_pattern(n)

print(pattern(5))




