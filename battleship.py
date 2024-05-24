'''
File: battleship.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: a program to read 2 text files,
        which respectively reads positions of ship
        by player 1 and guesses of player 2,
        and responds to all positions in game. 
'''

import sys

class GridPosition:
    '''
    Represents the grid as a 2Dlist.
    
    '''
    def __init__(self, x, y, ship):
        '''
         Initializes a GridPosition object.
        
        Args:
            x: The x-coordinate of the position.
            y: The y-coordinate of the position.
            ship: The ship occupying the position.

        Return:
            None
        '''
        self._x = x
        self._y = y
        self._ship = ship
        self._guess = 0

    def __str__(self):
        if self._ship == None:
            return "N"
        else:
            return self._ship.type
        
class Board:
    '''
    Represents the game board 
    with the ships placement.
    '''
    def __init__(self, list_ship, grid):
        '''
        Initializes a Board object.
        
        Args:
            list_ship: List of ships on the board.
            grid: 2D list representing the game grid.

        Return:
            None
        '''
        self._list_ship = list_ship
        self._grid = grid

    def guess(self, x, y):
        '''
        Processes a guess on the board.
        
        Args:
            x: The x-coordinate of the guessed position.
            y: The y-coordinate of the guessed position.
        
        Return:
            None
        '''
        if (x < 0 or y < 0 or x > 9 or y > 9):
            print("illegal guess")
        else:
            gridpos = self._grid[x][y]
            if gridpos._ship == None:
                if gridpos._guess != 0:
                    print("miss (again)")
                else:
                    print("miss")
                gridpos._guess = 1
            else:
                if gridpos._guess != 0:
                    print("hit (again)")
                else:
                    gridpos._ship._health -= 1
                    if gridpos._ship._health == 0:
                        print("{} sunk".format(gridpos._ship))
                    else:
                        print("hit")
                gridpos._guess = 1

class Ship:
    '''
    Represents a ship in the game.
    '''
    def __init__(self, list, diff):
        '''
        Initializes a Ship object.
        
        Args:
            list: List containing ship data.
            diff: other lines from the file.
        '''
        self._diff = diff
        self._gridpos = []
        self._type = list[0]
        self._first_x = int(list[1])
        self._first_y = int(list[2])
        self._final_x = int(list[3])
        self._final_y = int(list[4])
        self.take_gridpos()
        self.move_valid()
    
    def take_gridpos(self):
        '''
        Determines the positions occupied by the ship
        to find the size of the ship it has been hit.
        '''
        if (self._first_x != self._final_x) \
            and (self._final_y != self._first_y):
            print("ERROR: ship not horizontal or vertical: " + self._diff)
            sys.exit(0)

        if self._first_x == self._final_x:
            self._size = abs(self._first_y - self._final_y) + 1
            self._health = abs(self._first_y - self._final_y) + 1

            for i in range(self._size):
                if self._first_y < self._final_y:
                    self._gridpos.append((self._first_x,self._first_y + i))
                else:
                    self._gridpos.append((self._first_x, self._final_y + i))
        
        else:
            self._size = abs(self._first_x - self._final_x) + 1
            self._health = abs(self._first_x - self._final_x) + 1
            
            for i in range(self._size):
                if self._first_x < self._final_x:
                    self._gridpos.append((self._first_x + i,self._first_y))
                else:
                    self._gridpos.append((self._final_x + i, self._first_y))

    def move_valid(self):
        '''
        Validates the type of the ship based on its size.
        '''
        if (self._type == 'A' and self._size != 5) \
            or (self._type == 'B' and self._size != 4) \
            or (self._type == 'S' and self._size != 3) \
            or (self._type == 'D' and self._size != 3) \
            or (self._type == 'P' and self._size != 2):
            print( "ERROR: incorrect ship size: " + self._diff)
            sys.exit(0)
        
    def __str__(self):
        return self._type
    
def read_file(placement, guess):
    '''
    Reads ship placements and guesses from files and processes the game.
    
    Args:
        placement: List of strings containing ship placements.
        guess: List of strings containing guesses.
    '''
    list_ship = []
    grid = []

    for data in placement:
        diff = data
        data = data.split()
        ship = Ship(data, diff)
        for number in data[1:5]:
            if int(number) < 0 or int(number) > 9:
                print("ERROR: ship out-of-bounds: " + diff)
                sys.exit(0)
        if ship not in list_ship:
            list_ship.append(ship)
        elif ship in list_ship:
            print("ERROR: fleet composition incorrect")
            sys.exit(0)

    if len(list_ship) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)

    for i in range(10):
        col = []
        for j in range(10):
            data_pos = None
            for ship in list_ship:
                if (i,j) in ship._gridpos:
                    if data_pos != None:
                        print("ERROR: overlapping ship: " + ship._diff)
                        sys.exit(0)
                    data_pos = GridPosition(i,j,ship)
            if data_pos == None:
                data_pos = GridPosition(i,j,None)
            col.append(data_pos)
        grid.append(col)

    board = Board(list_ship, grid)
    for data in guess:
        data = data.split()
        board.guess(int(data[0]),int(data[1]))
        ships_alive = 0
        for ship in board._list_ship:
            if ship._health != 0:
                ships_alive += 1
        if ships_alive == 0:
            print("all ships sunk: game over")
            sys.exit(0)

def main():
    place = open(input()).readlines()
    guess = open(input()).readlines()
    read_file(place, guess)

main()