import dedupe.variables.number as number

def test_two_num_strings(pn):
    assert pn.comparator('1', '100') == 2

def test_two_num_strings_leading(pn):
    assert pn.comparator('$1', '+100') == 2
    assert pn.comparator('$1', 'foobar100') == 2
    assert pn.comparator('$0.1', 'foobar100') == 3

def test_two_num_strings_trailing(pn):
    assert pn.comparator('1', '+100.') == 2
    assert pn.comparator('1-', '100foo') == 2
    assert pn.comparator('0.1', '100-+') == 3

def test_non_num(pn):
    assert pn.comparator('foo', 'bar') is None
    assert pn.comparator('12', '100foo.') is None
    assert pn.comparator('.0.1', '100-+') is None

def test_predicates(pn):
    assert number.orderOfMagnitude('100') == ('2',)
    assert number.orderOfMagnitude('100foo') == ('2',)
    assert number.roundTo1('100') == ('100',)
    assert number.roundTo1('150') == ('200',)

