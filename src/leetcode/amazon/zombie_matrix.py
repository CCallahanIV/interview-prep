from typing import List
from collections import namedtuple

Position = namedtuple("Position", "row, col")

def _in_bounds(rows: int, columns: int, pos: Position) -> bool:
        return (0 <= pos.row < rows) and (0 <= pos.col < columns)

def _all_zombies(rows: int, columns: int, grid: List[List[int]]):
    return sum(
        [
            sum(row) for row in grid
        ]
    ) == (rows * columns)

def _get_adjacent_positions(rows: int, columns: int, curr: Position):
    next_moves = []
    for drow, dcol in [(0,1), (0,-1), (1, 0), (-1, 0)]:
        new_pos = Position(curr.row + drow, curr.col + dcol)
        if _in_bounds(new_pos):
            next_moves.append(new_pos)
    return next_moves

def _get_all_positions(rows: int, columns: int):
    all_positions = []
    for i in range(rows):
        for j in range(columns):
            all_positions.append(Position(i, j))
    return all_positions


def min_hours(rows: int, columns: int, grid: List[List[int]]) -> int:
    hours = 0
    # This is O(hours*N) since we will always iterate through the entire grid for every hour.
    while not _all_zombies(rows, columns, grid):
        victims = set()
        for pos in _get_all_positions(rows, columns):
            if grid[pos.row][pos.col] == 1:
                for adj_pos in _get_adjacent_positions(rows, columns, pos):
                    if grid[adj_pos.row][adj_pos.col] == 0:
                        victims.add(adj_pos)

        for victim in victims:
            grid[victim.row][victim.col] = 1
        hours += 1

    return hours


def min_hours_2(rows: int, columns: int, grid: List[List[int]]) -> int:
    """This time, we'll track new zombies as we go."""

    zombies = [Position(i, j) for i in range(rows) for j in range(columns) if grid[i][j] == 0]
    hours = 0
    while True:
        new = []
        for pos in zombies:
            for adj_pos in _get_adjacent_positions(rows, columns, pos):
                if grid[adj_pos.row][adj_pos.col] == 0:
                    grid[adj_pos.row][adj_pos.col] = 1
                    new.append(adj_pos)
                
        zombies = new
        if not zombies:
            # No new zombies - EVERYONE IS INFECTED
            break
        hours += 1
    
    return hours
