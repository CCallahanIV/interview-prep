from typing import List
from collections import namedtuple

Position = namedtuple("Position", "row, col")


def min_hours(rows: int, columns: int, grid: List[List[int]]) -> int:

    def _in_bounds(pos: Position) -> bool:
        return (0 <= pos.row < rows) and (0 <= pos.col < columns)

    def _all_zombies(grid: List[List[int]]):
        return sum(
            [
                sum(row) for row in grid
            ]
        ) == (rows * columns)
    
    def _get_adjacent_positions(curr):
        next_moves = []
        for drow, dcol in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            new_pos = Position(curr.row + drow, curr.col + dcol)
            if _in_bounds(new_pos):
                next_moves.append(new_pos)
        return next_moves

    def _get_all_positions():
        all_positions = []
        for i in range(rows):
            for j in range(columns):
                all_positions.append(Position(i, j))
        return all_positions

    hours = 0
    while not _all_zombies(grid):
        victims = set()
        for pos in _get_all_positions():
            if grid[pos.row][pos.col] == 1:
                for adj_pos in _get_adjacent_positions(pos):
                    if grid[adj_pos.row][adj_pos.col] == 0:
                        victims.add(adj_pos)

        for victim in victims:
            grid[victim.row][victim.col] = 1
        hours += 1

    return hours
