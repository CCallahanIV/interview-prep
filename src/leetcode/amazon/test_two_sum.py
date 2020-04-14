import pytest

from two_sum import two_sum_solution_brute_force, two_sum_solution

TEST_FUNCTIONS = [two_sum_solution_brute_force, two_sum_solution]

@pytest.mark.parametrize(
    "nums,target,exp",
    [
        [
            [1, 1, 2, 45, 46, 46],
            47,
            2
        ],
        [
            [1, 1],
            2,
            1
        ],
        [
            [1, 5, 1, 5],
            6,
            1
        ]
    ]
)
def test_two_sums_solution(nums, target, exp):
    for func in TEST_FUNCTIONS:
        assert func(nums, target) == exp