import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = grid.shape
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_node = (current[0]+dx, current[1]+dy)

            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols:
                if grid[next_node] == 1:
                    continue

                new_cost = cost[current] + 1

                if next_node not in cost or new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(open_list, (priority, next_node))
                    came_from[next_node] = current

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = came_from.get(node)
        if node is None:
            return []

    path.append(start)
    path.reverse()

    return path