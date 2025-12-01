with open("input.txt") as f:
    lines = f.read().split("\n")
    print(lines)
    lines_as_numbers = [int(line.replace("L", "-").replace("R", "+"))
                        for line in lines if line != ""]  # for some reason there's an empty line at the end of the file

dial = 50
zeros = 0

for line in lines_as_numbers:
    new_dial = dial + line
    
    # if the new dial value is between 100 and 199, it's gone through zero once
    # if it's between 200 and 299, twice, if between 300 and 399, three times, and so on
    # for the non-positives, it's like: between 0 and -99 is one time, between -100 and -199 is two,
    # and so on; if it's between 1 and 99, nothing has changed

    # the positive case is simply floor division (100 // 100 is 1, and so is 199 // 100)
    # the negative case is also floor division but you have to subtract one from the original number,
    # since if it's on zero, it has touched zero once.

    if new_dial > 0:
        zeros += new_dial // 100
    else:
        zeros -= (new_dial - 1) // 100  # -= as it can't touch zero negative times...
        if dial == 0:
            zeros -= 1  # as it will end up overcounting if the dial starts from zero

    print(f"current number of zeros is {zeros}, after rotating {line} from {dial} to {new_dial % 100}")
    dial = new_dial % 100

print(zeros)