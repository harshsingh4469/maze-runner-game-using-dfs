""" 
Maze Runner Game using Depth First Search (DFS)

Legend:
0 -> Path
1 -> Wall
S -> Start
E -> End
* -> Solution Path
"""

# Maze representation
maze = [
    ['S', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 'E']
]

ROWS = len(maze)
COLS = len(maze[0])

# Directions: Down, Up, Right, Left
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
path = []


def find_start(maze):
    """Find the starting point in the maze"""
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == 'S':
                return i, j
    return None


def is_valid(x, y):
    """Check if the move is within bounds and valid"""
    return (
        0 <= x < ROWS and
        0 <= y < COLS and
        maze[x][y] != 1 and
        not visited[x][y]
    )


def dfs(x, y):
    """
    Depth First Search algorithm to find path from Start to End
    """
    # Base Case: If End is reached
    if maze[x][y] == 'E':
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))

    # Explore neighbors
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            if dfs(nx, ny):
                return True

    # Backtracking
    path.pop()
    return False


def mark_solution_path():
    """Mark the solution path in the maze"""
    for x, y in path:
        if maze[x][y] not in ('S', 'E'):
            maze[x][y] = '*'


def print_maze():
    """Print the maze"""
    for row in maze:
        print(" ".join(str(cell) for cell in row))


def main():
    start = find_start(maze)
    if not start:
        print("Start position not found!")
        return

    sx, sy = start

    if dfs(sx, sy):
        mark_solution_path()
        print("\n✅ Path Found!\n")
    else:
        print("\n❌ No Path Exists!\n")

    print_maze()


if __name__ == "__main__":
    main()
