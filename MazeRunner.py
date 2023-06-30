import random

# Constants
WALL = "#"
PATH = " "
START = "S"
END = "E"

# Function to generate the maze
def generate_maze(width, height):
    maze = [[WALL] * width for _ in range(height)]
    stack = []
    
    # Recursive backtracking algorithm
    def backtrack(x, y):
        maze[y][x] = PATH
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + (dx * 2), y + (dy * 2)
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == WALL:
                maze[y + dy][x + dx] = PATH
                stack.append((nx, ny))
                backtrack(nx, ny)
    
    # Start generating the maze from a random position
    global start_x,start_y;
    start_x = random.randrange(0, width, 2)
    start_y = random.randrange(0, height, 2)
    backtrack(start_x, start_y)
    
    # Set the start and end points
    maze[start_y][start_x] = START
    maze[height - 1][width - 1] = END
    
    return maze

# Function to display the maze on the terminal
def display_maze(maze):
    for row in maze:
        print(" ".join(row))

# Main code
width = 21  # Adjust the width of the maze
height = 21  # Adjust the height of the maze

maze = generate_maze(width, height)
display_maze(maze)

# the code for generate the maze is complete but solving it is still an issue 
#any idea on how to solve it..?

# # Constants
# WALL = "#"
# PATH = " "
# START = "S"
# END = "E"
# VISITED = "."

# # Function to solve the maze
# def solve_maze(maze, x, y):
#     # Base cases
#     if maze[y][x] == END:
#         return True
#     if maze[y][x] in [WALL, VISITED]:
#         return False

#     # Mark the current cell as visited
#     maze[y][x] = VISITED

#     # Recursive depth-first search in all four directions
#     if (
#         solve_maze(maze, x + 1, y) or solve_maze(maze, x - 1, y) or
#         solve_maze(maze, x, y + 1) or solve_maze(maze, x, y - 1)):
#         return True

#     # Mark the current cell as part of the path
#     maze[y][x] = PATH
#     return False

# # Function to display the solved maze
# def display_maze(maze):
#     for row in maze:
#         print("".join(row))

# # Main code
# width = 21  # Adjust the width of the maze
# height = 21  # Adjust the height of the maze

# maze = generate_maze(width, height)  # Generate the maze
# # start_x, start_y = get_start_position(maze)  # Get the start position

# solve_maze(maze, start_x, start_y)  # Solve the maze
# display_maze(maze)  # Display the solved maze
