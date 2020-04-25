import pytest

from leetcode.amazon.gen_paren import gen_paren_solution

@pytest.mark.parametrize(
    "n,exp",
    [
        (
            3,
            [
                "((()))",
                "(()())",
                "(())()",
                "()(())",
                "()()()"
            ],
        ),
        (
            2,
            [
                "(())",
                "()()"
            ]
        ),
        (
            1,
            [
                "()"
            ]
        ),
        (
            0,
            []
        )
    ]
)
def test_gen_paren(n, exp):
    assert gen_paren_solution(n) == exp
