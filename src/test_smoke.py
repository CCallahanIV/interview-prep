import pytest
from smoke import smoke_test

@pytest.mark.parametrize(
    "param",
    [True]
)
def test_tests(param):
    assert smoke_test(param)
