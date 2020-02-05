import random

grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
a = 'O'
b = 'X'


def checkWinner(grid):
    # First row player 1
    if grid[0][0] == a and grid[0][1] == a and grid[0][2] == a:
        return -1
    # First row player 2
    if grid[0][0] == b and grid[0][1] == b and grid[0][2] == b:
        return 1
    # Second row player 1
    if grid[1][0] == a and grid[1][1] == a and grid[1][2] == a:
        return -1
    # Second row player 2
    if grid[1][0] == b and grid[1][1] == b and grid[1][2] == b:
        return 1
    # Third row player 1
    if grid[2][0] == a and grid[2][1] == a and grid[2][2] == a:
        return -1
    # Third row player 2
    if grid[2][0] == b and grid[2][1] == b and grid[2][2] == b:
        return 1
    # First column player 1
    if grid[0][0] == a and grid[1][0] == a and grid[2][0] == a:
        return -1
    # First column player 2
    if grid[0][0] == b and grid[1][0] == b and grid[2][0] == b:
        return 1
    # Second column player 1
    if grid[0][1] == a and grid[1][1] == a and grid[2][1] == a:
        return -1
    # Second column player 2
    if grid[0][1] == b and grid[1][1] == b and grid[2][1] == b:
        return 1
    # Third column player 1
    if grid[0][2] == a and grid[1][2] == a and grid[2][2] == a:
        return -1
    # Third column player 2
    if grid[0][2] == b and grid[1][2] == b and grid[2][2] == b:
        return 1
    # Major diagonal player 1
    if grid[0][0] == a and grid[1][1] == a and grid[2][2] == a:
        return -1
    # Major diagonal player 2
    if grid[0][0] == b and grid[1][1] == b and grid[2][2] == b:
        return 1
    # Minor diagonal player 1
    if grid[0][2] == a and grid[1][1] == a and grid[2][0] == a:
        return -1
    # Minor diagonal player 2
    if grid[0][2] == b and grid[1][1] == b and grid[2][0] == b:
        return 1
    for i in grid:
        for j in i:
            if j == '-':
                return 0
    return 99


def printGrid(grid):
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()
    print()


def markMyEntry(position, player):
    if position not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
        return False
    if player == 1:
        symbol = a
    else:
        symbol = b
    if position == 'a':
        if grid[0][0] != '-':
            return False
        grid[0][0] = symbol
        return True
    if position == 'b':
        if grid[0][1] != '-':
            return False
        grid[0][1] = symbol
        return True
    if position == 'c':
        if grid[0][2] != '-':
            return False
        grid[0][2] = symbol
        return True
    if position == 'd':
        if grid[1][0] != '-':
            return False
        grid[1][0] = symbol
        return True
    if position == 'e':
        if grid[1][1] != '-':
            return False
        grid[1][1] = symbol
        return True
    if position == 'f':
        if grid[1][2] != '-':
            return False
        grid[1][2] = symbol
        return True
    if position == 'g':
        if grid[2][0] != '-':
            return False
        grid[2][0] = symbol
        return True
    if position == 'h':
        if grid[2][1] != '-':
            return False
        grid[2][1] = symbol
        return True
    if position == 'i':
        if grid[2][2] != '-':
            return False
        grid[2][2] = symbol
        return True


def twoPlayerGame():
    printGrid(grid)
    chance = 1
    while checkWinner(grid) == 0:
        print("Enter a location: ",end=' ')
        position = input()
        if chance == 1:
            if markMyEntry(position, 1):
                chance = 2
            else:
                print("Invalid Move")
        else:
            if markMyEntry(position, 2):
                chance = 1
            else:
                print("Invalid Move")
        printGrid(grid)
        if (checkWinner(grid) == 1):
            print("Winner is B")
        elif (checkWinner(grid) == -1):
            print("Winner is A")
        elif (checkWinner(grid) == 99):
            print("Game Drawn")

def getARandomLocation():
    return random.choice(['a','b','c','d','e','f','g','h','i'])


def onePlayerGameEasy():
    printGrid(grid)
    chance = 1
    while checkWinner(grid) == 0:
        if chance == 1:
            print("Enter a location: ", end=' ')
            position = input()
            if markMyEntry(position, 1):
                chance = 2
            else:
                print("Invalid Move")
        else:
            while(1):
                position = getARandomLocation()
                if markMyEntry(position, 2):
                    chance = 1
                    break
                # print("Invalid Move")
        printGrid(grid)
        if (checkWinner(grid) == 1):
            print("Winner is B")
        elif (checkWinner(grid) == -1):
            print("Winner is A")
        elif (checkWinner(grid) == 99):
            print("Game Drawn")

if __name__ == '__main__':
    print("Which mode do you want to play the game in: ")
    print("1. 1-Player (Easy)")
    print("2. 2-Player")
    choice = int(input())
    if choice == 1:
        onePlayerGameEasy()
    elif choice == 2:
        twoPlayerGame()
    else:
        print("Invalid choice")