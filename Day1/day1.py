'''
In the first Advent of Code 2021 puzzle, there is a list of numbers. 
Part 1 Goal is to find the number of instances where a number is larger than the previous number.
Part 2 includes a sliding window of 3 and calculate the sums, creating a new list. 
    Goal is to find the number of instances in the new list where a number is larger than the previous number.

Since input data is custom for each user, mine way extracted from the website and is stored in the input.txt file.

'''
def calculate_increase_counts(xs):
    '''
    Given a list of numbers calculates the count of instances where a given number is larger than previous number.
    '''
    differences = [i-j for i,j in zip(xs[1:], xs[:-1])]
    positive_differences = [i for i in differences if i > 0]
    return len(positive_differences)

def calculate_sliding_sum(xs, sliding_window):
    '''
    Returns the sum of the first "sliding_window" number of elements
    '''
    return sum(xs[:sliding_window])

# Start with loading the input data
with open("input.txt") as f:
    raw_data = f.read()

# The string is converted to a list and the differences calculated.
number_list = [int(i) for i in raw_data.split("\n")]
# Number of positive differences is counted from the difference list.
print(calculate_increase_counts(number_list))

# Part 2
sliding_window = 3
part2_input = number_list.copy()
sliding_sums = []
# Sliding sums are calculated and stored in a list, the increase is calculated on this resulting list
while len(part2_input) >= sliding_window:
    sliding_sums.append(calculate_sliding_sum(part2_input, sliding_window))
    part2_input = part2_input[1:]

print(calculate_increase_counts(sliding_sums))