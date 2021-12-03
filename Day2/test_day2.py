import day2

xs = day2.get_data("test_input.txt")

def test_one():
    assert day2.calc_final_position(day2.decode_direction(xs)) == 150

def test_two():
    assert day2.calc_final_position_aim(day2.decode_direction(xs)) == 900
