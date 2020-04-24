from collections import deque, namedtuple
from math import inf
from typing import List

def treasure_island_recursive_solution(treasure_map: List[List[str]]) -> int:
    visited = [[inf for _ in range(len(treasure_map[0]))] for _ in range(len(treasure_map))]
    
    def out_of_bounds(val):
        return val < 0 or val >= len(treasure_map)

    def visit(i, j, steps=0):
        if out_of_bounds(i) or out_of_bounds(j):
            return
        
        if treasure_map[i][j] == "D":
            return

        if treasure_map[i][j] == "X":
            return steps
        
        if steps < visited[i][j]:
            visited[i][j] = steps
        else: return

        steps += 1
        left = visit(i - 1, j, steps)
        right = visit(i + 1, j, steps)
        up = visit(i, j + 1, steps)
        down = visit(i, j - 1, steps)

        results = [
            val for val in [left, right, up, down]
            if val is not None
        ]
        if results:
            return min(results)
        else:
            return None
    
    return visit(0, 0)


Location = namedtuple('Location', 'i, j, steps')

def treasure_island_bfs_solution(treasure_map: List[List[str]]) -> int:
    min_steps = inf
    visited = [[inf for _ in range(len(treasure_map[0]))] for _ in range(len(treasure_map))]
    def out_of_bounds(loc: Location) -> bool:
        def _check_coord(val: int) -> bool:
            return val < 0 or val >= len(treasure_map)
        return _check_coord(loc.i) or _check_coord(loc.j)

    dq = deque()
    dq.append(Location(0, 0, 0))
    while dq:
        curr = dq.popleft()
        
        if treasure_map[curr.i][curr.j] == "X":
            min_steps = min(curr.steps, min_steps)
            continue

        if treasure_map[curr.i][curr.j] == "D":
            continue

        if curr.steps < visited[curr.i][curr.j]:
            visited[curr.i][curr.j] = curr.steps
        else: continue

        next_moves = [
            Location(curr.i + 1, curr.j, curr.steps + 1),
            Location(curr.i - 1, curr.j, curr.steps + 1),
            Location(curr.i, curr.j + 1, curr.steps + 1),
            Location(curr.i, curr.j - 1, curr.steps + 1)
        ]
        for move in next_moves:
            if not out_of_bounds(move):
                dq.append(move)

    return min_steps