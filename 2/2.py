from math import floor

def is_invalid_1(id):
    idstr = str(id)
    id_length = len(idstr)
    if id_length % 2 == 1:
        return False
    
    midpoint = len(idstr) // 2
    first_half, second_half = idstr[:midpoint], idstr[midpoint:]

    return first_half == second_half

def is_invalid_2(id):
    idstr = str(id)
    id_length = len(idstr)
    for length in range(1, id_length // 2 + 1):  # "length" here is the possible length of the repeated string
        if len(idstr) % length != 0:
            continue  # no point testing for repetitions of length 2 in a string with five characters, for example

        if idstr[:length] * (id_length // length) == idstr:
            return True  # we've found a string composed entirely of repeats
    
    return False

with open("input.txt") as f:
    ranges = []
    for item in f.read().split(","):
        start, end = item.split("-")
        ranges.append((int(start), int(end)))

def add_ids(test):
    invalid_id_sum = 0
    for r in ranges:
        invalid_ids_in_range = 0
        for i in range(r[0], r[1] + 1):
            if test(i):
                invalid_id_sum += i
    return invalid_id_sum

print(f"answer for 2-1: the invalid IDs add up to {add_ids(is_invalid_1)} in total")
print(f"answer for 2-2: the invalid IDs add up to {add_ids(is_invalid_2)} in total")