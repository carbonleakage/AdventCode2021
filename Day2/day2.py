'''
The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
'''

def get_data(fp):
    with open(fp) as f:
        contents_raw = f.read().split("\n")
        contents_instructions = [(i.split()[0], int(i.split()[1])) for i in contents_raw]
        return contents_instructions

def decode_direction(xs):
    direction_matrix = {
        "down":1,
        "up":-1
    }
    ys = []
    for (i,j) in xs:
        if i == "forward":
            ys.append((i,j))
        else:
            ys.append(("depth",j*direction_matrix[i]))
    return ys

def calc_final_position(xs):
    horizontal = 0
    depth = 0
    for (i,j) in xs:
        if i == "forward":
            horizontal += j
        else:
            depth += j
    return horizontal*depth

def calc_final_position_aim(xs):
    horizontal = 0
    depth = 0
    aim = 0
    for (i,j) in xs:
        if i == "forward":
            horizontal += j
            depth += aim * j
        else:
            aim += j
    return horizontal*depth

print(calc_final_position(decode_direction(get_data("input.txt"))))
print(calc_final_position_aim(decode_direction(get_data("input.txt"))))