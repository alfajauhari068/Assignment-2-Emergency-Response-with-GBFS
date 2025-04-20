def gbfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    open_list = [(heuristic_manhattan(start, goal), start[0], start[1])]
    visited = set()
    came_from = {}

    while open_list:
        open_list.sort()  
        _, x, y = open_list.pop(0)
        if (x, y) == goal:
            path = []
            while (x, y) in came_from:
                path.append((x, y))
                x, y = came_from[(x, y)]
            path.append((x, y))
            return path[::-1]
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'T':
                if (nx, ny) not in visited:
                    h = heuristic_manhattan((nx, ny), goal)
                    open_list.append((h, nx, ny))
                    came_from[(nx, ny)] = (x, y)  
    return None

def heuristic_manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


grid = [
    ['S', '.', '.', 'T'],
    ['T', '.', 'T', '.'],
    ['.', '.', '.', 'H']
]
start = (0, 0)
goal = (2, 3)
path = gbfs(grid, start, goal)
print("Jalur GBFS:", path)  # Output: [(0,0) → (0,1) → (1,1) → (2,1) → (2,2) → (2,3)]
