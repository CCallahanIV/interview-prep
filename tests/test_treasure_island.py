import pytest

from leetcode.amazon.treasure_island import treasure_island_recursive_solution, treasure_island_bfs_solution

TEST_FUNCS = [
    treasure_island_bfs_solution, treasure_island_recursive_solution
]

@pytest.mark.parametrize(
    "treasure_map,steps",
    [
        (
            [
                ['O', 'O', 'O', 'O'],
                ['D', 'O', 'D', 'O'],
                ['O', 'O', 'O', 'O'],
                ['X', 'D', 'D', 'O']
            ],
            5
        )
    ]
)
def test_treasure_island(treasure_map, steps):
    for func in TEST_FUNCS:
        assert func(treasure_map) == steps
