from day1 import calculate_sliding_sum

xs = [1,2,3,4]
def test_two_elements():
    assert calculate_sliding_sum(xs,2) == 3

def test_three_elements():
    assert calculate_sliding_sum(xs,3) == 6

def test_four_elements():
    assert calculate_sliding_sum(xs,4) == 10