import random

def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    grid_letters = "abcdefghijklmnopqrstuvwxyz"
    grid = []
    for row in range(grid_size):
        row = []
        for letter in range(grid_size):
            index = random.randint(0,len(grid_letters)-1)
            row.append(grid_letters[index])
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        result_grid = ",".join(row)
        print(result_grid)

def main():
    grid_size = init()
    grid_created = make_grid(grid_size)
    print_grid(grid_created)

main()