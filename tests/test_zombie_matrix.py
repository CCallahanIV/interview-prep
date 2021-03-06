from copy import deepcopy

import pytest

from leetcode.amazon.zombie_matrix import min_hours, min_hours_2

TEST_FUNCTIONS = [min_hours, min_hours_2]

@pytest.mark.parametrize(
    "rows,columns,grid,exp",
    [
        (
            4,
            5,
            [
                [0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]
            ],
            2
        ),
    ]
)
def test_min_hours(rows, columns, grid, exp):
    for func in TEST_FUNCTIONS:
        assert func(rows, columns, deepcopy(grid)) == exp
