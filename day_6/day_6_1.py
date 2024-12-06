def parse_maze(maze_text):
    lines = [line.strip() for line in maze_text.split('\n')]
    grid = [list(line) for line in lines]
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return grid, (x, y), 'UP'
    

def is_valid_move(grid, pos):
    x, y = pos
    return grid[y][x] != '#'

def turn_right(direction):
    directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    return directions[(directions.index(direction) + 1) % 4]

def solve_maze(maze_text):
    grid, (x, y), direction = parse_maze(maze_text)
    visited_positions = set()
    offsets = {
        'DOWN': (0, 1),
        'UP': (0, -1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0)
    }
    
    while 0 <= y < len(grid[0]) and 0<= x < len(grid):
        print(len(visited_positions))
        visited_positions.add((x, y))
        
        dx, dy = offsets[direction]
        new_x, new_y = x + dx, y + dy
        
        if is_valid_move(grid, (new_x, new_y)):
            x, y = new_x, new_y 
        else:
            direction = turn_right(direction)
    
    return len(visited_positions)

if __name__ == "__main__":
    with open("puzzle_inputs/day_6.txt", "r") as file:
        maze_text = file.read()

    print(solve_maze(maze_text))
