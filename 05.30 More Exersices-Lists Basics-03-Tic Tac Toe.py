# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
#
# Legend:
#
# · 0 - empty space
#
# · 1 - first player move
#
# · 2 - second player move
#
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins,
# print "Second player won". Otherwise, print "Draw!".

row1_input = input().split()
row2_input = input().split()
row3_input = input().split()

row1 = []
row2 = []
row3 = []

for value in row1_input:
    row1.append(int(value))

for value in row2_input:
    row2.append(int(value))

for value in row3_input:
    row3.append(int(value))

board = [row1, row2, row3]


def check_winner(player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


if check_winner(1):
    print("First player won")
elif check_winner(2):
    print("Second player won")
else:
    print("Draw!")
