from dedupe.variables import number
import pytest

@pytest.fixture
def pn():
    return number.PositiveNumberType({'field': 'foo'})
