import numpy
import sys


def solve_task2(input_matrix):
    return conquer(input_matrix)


input_arg = sys.argv[1]
def run_program(filename=input_arg):
    input_matrix = numpy.genfromtxt(filename, dtype='str')
    solution = solve_task2(input_matrix)
    numpy.savetxt('output_for_task2.txt', solution, fmt='%s')


def conquer(grid):
    dots = numpy.where(grid == '.')
    grid[dots] = 'T'

    find_edgy(grid)
    conquered = numpy.where(grid == 'T')
    grid[conquered] = 'X'
    return grid


def find_connected(grid, start):
    # Recursive function
    x, y = start
    grid_x, grid_y = len(grid), len(grid[0])
    # Base case
    if x < 0 or x >= grid_x or y < 0 or y >= grid_y:
        return

    if grid[start] != 'T':
        return

    grid[start] = '.'

    find_connected(grid, (x-1, y))
    find_connected(grid, (x+1, y))
    find_connected(grid, (x, y-1))
    find_connected(grid, (x, y+1))


def find_edgy(grid):
    # Traverse top, bottom, left and right edges so that if there exists an exit route
    rows, cols = len(grid), len(grid[0])

    # top and bottom
    for i in range(cols):
        if grid[(0, i)] == 'T':  # exit route, find all connected T's
            find_connected(grid, (0, i))

        if grid[(rows-1, i)] == 'T':
            find_connected(grid, (rows-1, i))

    # left and right
    for i in range(rows):
        if grid[(i, 0)] == 'T':  # exit route, find all connected T's
            find_connected(grid, (i, 0))

        if grid[(i, cols-1)] == 'T':
            find_connected(grid, (i, cols-1))


run_program()
