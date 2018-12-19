import heapq
import sys
import numpy

def solve_task1(input_matrix):
    return a_star(input_matrix)


input_arg = sys.argv[1]
def run_program(file_name=input_arg):
    input_matrix = numpy.genfromtxt(file_name, dtype=str)
    print(solve_task1(input_matrix))


def a_star(grid):

    vertices = find_start_goal(grid=grid)
    start = vertices['start']
    goal = vertices['goal']

    # h: heuristic from current node to goal (L_inf norm)
    # g: exact cost moving from start to the current node (exact cost)

    open = [(0, start)]
    heapq.heapify(open)
    closed = {}
    closed[start] = 0

    while len(open) != 0:

        current = heapq.heappop(open)

        if current[1] == goal:
            break

        neighbors = find_neighbors(current=current[1], grid=grid)

        for n in neighbors:
            cost = closed[current[1]] + movement_cost(current=current[1], neighbor=n)

            if n not in closed or cost < closed[n]:
                closed[n] = cost
                f = cost + heuristic(n, goal)
                heapq.heappush(open, (f, n))

    if goal in closed:
        return closed[goal]
    else:
        return 'No path found!'


def movement_cost(current, neighbor):
    c_x, c_y = current[0], current[1]
    n_x, n_y = neighbor[0], neighbor[1]

    dx = n_x - c_x
    dy = n_y - c_y

    cost = -1
    if dx != 0:
        cost = 6

    if dy != 0:
        cost = 5

    if dx != 0 and dy != 0:
        cost = 10

    return cost


def find_neighbors(current, grid):
    # Discard obstacles and invalid indices
    # Consider 8-neighborhood
    x, y = current[0], current[1]
    neighbors = []

    x_lower = x - 1 >= 0
    x_upper = x + 1 < len(grid)
    y_lower = y - 1 >= 0
    y_upper = y + 1 < len(grid[0])

    if x_lower and grid[x-1][y] != '*':
        neighbors.append((x-1, y))

    if x_upper and grid[x+1][y] != '*':
        neighbors.append((x+1, y))

    if y_lower and grid[x][y-1] != '*':
        neighbors.append((x, y-1))

    if y_upper and grid[x][y+1] != '*':
        neighbors.append((x, y+1))

    if x_lower and y_lower and grid[x-1][y-1] != '*':
        neighbors.append((x-1, y-1))

    if x_lower and y_upper and grid[x-1][y+1] != '*':
        neighbors.append((x-1, y+1))

    if x_upper and y_lower and grid[x+1][y-1] != '*':
        neighbors.append((x+1, y-1))

    if x_upper and y_upper and grid[x+1][y+1] != '*':
        neighbors.append((x+1, y+1))

    return neighbors


def heuristic(current, goal):
    # Chebyshev distance
    d1 = 1
    d2 = 1

    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])

    return d1 * (dx + dy) + (d2 - 2*d1) * min(dx, dy)


def find_start_goal(grid):
    start = (-1, -1)
    goal = (-1, -1)
    for (i, row) in enumerate(grid):
        for (j, c) in enumerate(row):
            if c == 'R':
                start = (i, j)

            if c == 'X':
                goal = (i, j)

    return {
        'start': start,
        'goal': goal
    }

run_program()