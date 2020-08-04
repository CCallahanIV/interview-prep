import pytest

from algorithms.sorting.selection_sort import sort


@pytest.mark.parametrize(
    "arr",
    [
        (
            [51, 71, 17, 42]
        ),
        (
            [16, 12, 10, 24]
        ),
        (
            []
        ),
        (
            [1]
        ),
        (
            [-1, 0, 20, 3]
        )
    ]
)
def test_selection_sort(arr):
    sort(arr)
    assert arr == sorted(arr)
