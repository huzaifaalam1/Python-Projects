'''
File: word_search.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120 
Purpose: The program reads a grid of letter along with a
    list of words.The program then generates a word 
    search grid finding the words in horizontal, 
    vertical and diagonal in both forward and 
    backward direction. It then prints the list of words.
'''
def get_word_list(words_file):
    '''
    the function reads a list of words from a file
    Parameter: words_file is a file containing the words
    Returns: A list of the words in lower case
    '''
    # opens the file in read mode
    file = open(words_file,"r")
    words = []
    for word in file:
        words.append(word.strip().lower())
    file.close()
    return words

def get_grid_letters(grid_file):
    '''
    the function reads a grid of letters from a file
    Parameter: grid_file is a file containing the letters
    Returns: a list of the grid of the letters
    '''
    # opens the file in read mode
    file = open(grid_file, 'r')
    grid = [] 
    for line in file:
        grid.append(line.split())
    file.close()
    return grid

def find_hor_words(word_list,grid):
    '''
    the function searches for words horizontally.
    it searches both forwards and in reverse.
    Parameters:
        word_list is the list of the words to find
        grid is the 2D list to find the words in
    Returns:
        the list of the words found in the grid
    '''
    horizontal_words = []
    # Searches left-to-right
    for row in grid:
        for i in range(len(row)):
            for length in range(3, len(row)-i+1):
                seq = row[i:i+length]
                word = ''.join(seq).lower()
                if word in word_list:
                    if word not in horizontal_words:
                        horizontal_words.append(''.join(seq))
    # Searches right-to-left
    for row in grid:
        row_reversed = row[::-1]
        for i in range(len(row_reversed)):
            for length in range(3, len(row_reversed)-i+1):
                seq = row_reversed[i:i+length]
                word = ''.join(seq).lower()
                if word in word_list:
                    if word not in horizontal_words:
                        horizontal_words.append(''.join(seq))

    return horizontal_words

def find_vert_words(word_list, grid):
    vertical_words = []
    # Searches up-to-down
    for col in range(len(grid)):
        for i in range(len(grid[col][0])):
            column = []
            for row in grid:
                column.append(row[col])
            for i in range(len(column)):
                for length in range(3,len(column)-i+1):
                    seq = column[i:i+length]
                    word = ''.join(seq).lower()
                    if word in word_list:
                        if word not in vertical_words:
                            vertical_words.append(''.join(seq))
    # Searches bottom-to-up
    for col in range(len(grid)):
        for i in range(len(grid[col][0])):
            column_reversed = []
            for letter in range(len(grid) - 1, -1, -1):
                column_reversed.append(grid[letter][col])
            for i in range(len(column_reversed)):
                for length in range(3,len(column_reversed)-i+1):
                    seq = column_reversed[i:i+length]
                    word = ''.join(seq).lower()
                    if word in word_list:
                        if word not in vertical_words:
                            vertical_words.append(''.join(seq))

    return vertical_words

def find_diag_words(word_list, grid):
    '''
    this function searches the words in the list diagonally
    Parameteres:
        word_list is the list of the words to find
        grid is the 2D list to find the words in
    Returns:
        the list of the words found in the grid
    '''
    diagonal_words = []
    # Searches diagonally
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for length in range(3,min(len(grid)-i,len(grid[0])-j)+1):
                seq = []
                for k in range(length):
                    seq.append(grid[i + k][j + k])
                word = ''.join(seq).lower()
                if word in word_list:
                    if word not in diagonal_words:
                        diagonal_words.append(''.join(seq))

    return diagonal_words

def print_words(words):
    '''
    the function prints each word in the list
    Parameter: a list of words
    Returns: Prints the list of words
    '''
    for each_word in words:
        print(each_word)

def main():
    ''''
    this function helps read input files
    Parameters: None
    Returns: Nothing
    '''
    words_file = input().strip()
    grid_file = input().strip()

    word_list = get_word_list(words_file)
    grid = get_grid_letters(grid_file)

    all_words_found = []

    hor_output = find_hor_words(word_list, grid)
    vert_output = find_vert_words(word_list, grid)
    diag_output = find_diag_words(word_list, grid)

    all_words_found.extend(hor_output)
    all_words_found.extend(vert_output)
    all_words_found.extend(diag_output)

    all_words_found.sort()
    print_words(all_words_found)

main()







            


