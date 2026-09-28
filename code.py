import heapq
import time
from collections import deque

def generate_grid(size=1000):
    """Generates a grid with obstacles."""
    grid = [[0] * size for _ in range(size)]
    # Add vertical walls with gaps to force deep paths
    for row in range(size):
        if row % 2 == 1:
            for col in range(size - 1):
                grid[row][col] = 1  # 1 represents wall/obstacle
    return grid

def get_neighbors(node, size):
    r, c = node
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size:
            neighbors.append((nr, nc))
    return neighbors

def bfs(grid, start, goal):
    """Breadth-First Search implementation using deque."""
    size = len(grid)
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        for neighbor in get_neighbors(current, size):
            r, c = neighbor
            if grid[r][c] == 0 and neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    # Reconstruct path
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = visited.get(curr)
    return path[::-1]

def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """A* Search implementation using a Priority Queue."""
    size = len(grid)
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for neighbor in get_neighbors(current, size):
            r, c = neighbor
            if grid[r][c] == 1:
                continue

            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    # Reconstruct path
    path = []
    curr = goal
    while curr in came_from or curr == start:
        path.append(curr)
        curr = came_from.get(curr)
        if curr is None:
            break
    return path[::-1]

def main():
    GRID_SIZE = 800
    START = (0, 0)
    GOAL = (GRID_SIZE - 1, GRID_SIZE - 1)

    print("Generating Grid...")
    grid = generate_grid(GRID_SIZE)

    print("Running repeated searches for profiling (Ctrl+C to stop)...")
    # Loop continuously so py-spy has enough sampling time
    for i in range(20):
        print(f"Iteration {i+1}/20")
        
        # Run BFS
        bfs_path = bfs(grid, START, GOAL)
        
        # Run A*
        astar_path = a_star(grid, START, GOAL)

if __name__ == "__main__":
    main()
