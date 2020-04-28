import pytest

from leetcode.amazon.zombie_matrix import min_hours

TEST_FUNCTIONS = [min_hours]

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
        assert func(rows, columns, grid) == exp
