# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Sydnee Ramirez
# Created: 2018-11-8

global board 
symbol = [ " ", "x", "o" ]

def printRow(row):
    output = "|"
    for cell in row:
        output += " " + symbol[cell] + " |"
    print(output)

def printBoard(board):
    for i in range (0,3):
        print("+-----------+")
        printRow(board[i])
    print("+-----------+")

def markBoard(board, row, col, player):
    if board [row][col] == 0:
        board[row][col] = player
    else:
        print("Pick a different spot")
        getPlayerMove()
        return False
    
def getPlayerMove():
   row,col = input("Please enter a row and column").split(",")
   return (int(row),int(col))

def hasBlanks(board):
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == 0:
               return True
    return False

def main():
    player = 1
    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 +1 # switch player for next turn
main()

