# Created by: Ian McCourt
import heapq


def create_grid_with_edges(rows, cols):
    grid = {}
    for r in range(rows):
        for c in range(cols):
            grid[(r, c)] = []
            if r > 0:
                grid[(r, c)].append((r-1, c))
            if r < rows - 1:
                grid[(r, c)].append((r+1, c))
            if c > 0:
                grid[(r, c)].append((r, c-1))
            if c < cols - 1:
                grid[(r, c)].append((r, c+1))
    return grid


def add_walls(grid, walls):
    for (node1, node2) in walls:
        if node2 in grid[node1]:
            grid[node1].remove(node2)
        if node1 in grid[node2]:
            grid[node2].remove(node1)


# Example 9x9 grid with some walls
grid = create_grid_with_edges(9, 8)
walls = [
    ((1, 5), (1, 6)),
    ((1, 5), (2, 5)),
    ((1, 4), (2, 4)),
    ((2, 3), (2, 4)),
    ((3, 3), (3, 4)),
    ((3, 3), (4, 3)),
    ((4, 3), (4, 4)),
    ((3, 2), (4, 2)),
    ((4, 1), (4, 2)),
    ((5, 1), (5, 2)),
    ((6, 1), (6, 2)),
    ((7, 1), (7, 2)),
    ((6, 2), (7, 2)),
    ((6, 3), (7, 3)),
    ((6, 4), (7, 4)),
    ((3, 6), (4, 6)),
    ((4, 5), (4, 6)),
    ((5, 5), (5, 6)),
    ((6, 5), (6, 6)),
    ((7, 5), (7, 6)),
    ((5, 7), (6, 7))
]

add_walls(grid, walls)


def get_neighbors(node, grid):
    return grid[node]


def manhattan_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid, start, goal):

    pq = [(0, start)]

    g_score = {start: 0}

    came_from = {}

    def heuristic(node, goal):
        return manhattan_distance(node, goal)

    while pq:
        current_f, current_node = heapq.heappop(pq)

        # If the goal is reached
        if current_node == goal:
            # Reconstruct the path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        # Explore neighbors
        for neighbor in get_neighbors(current_node, grid):
            tentative_g_score = g_score[current_node] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None


start = (0, 0)
goal = (8, 7)
path = a_star_search(grid, start, goal)
print("Path found:", path)

