import pytest

from leetcode.amazon.top_k_keywords import top_k_keywords

TEST_FUNCTIONS = [top_k_keywords]

@pytest.mark.parametrize(
    "k,keywords,reviews,exp",
    [
        (
            2,
            ["anacell", "cetracular", "betacellular"],
            [
                "Anacell provides the best services in the city",
                "betacellular has awesome services",
                "Best services provided by anacell, everyone should use anacell",
            ],
            ["anacell", "betacellular"]
        ),
        (
            2,
            ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
            [
                "I love anacell Best services; Best services provided by anacell",
                "betacellular has great services",
                "deltacellular provides much better services than betacellular",
                "cetracular is worse than anacell",
                "Betacellular is better than deltacellular.",
            ],
            ["betacellular", "anacell"]
        )
    ]
)
def test_top_k_keywords(k, keywords, reviews, exp):
    for func in TEST_FUNCTIONS:
        assert func(k, keywords, reviews) == exp
