import pytest

from leetcode.microsoft.equal_sums import solution

TEST_FUNCS = [
    solution
]

@pytest.mark.parametrize(
    "arr,exp",
    [
        (
            [51, 71, 17, 42],
            93
        ),
        (
            [42, 33, 60],
            102
        ),
        (
            [51, 32, 43],
            -1
        )
    ]
    
)
def test_equal_sums(arr, exp):
    for func in TEST_FUNCS:
        assert func(arr) == exp
