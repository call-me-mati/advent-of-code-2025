with open("input.txt") as f:
    lines = f.read().split("\n")

lines_as_numbers = [int(line.replace("L", "-").replace("R", "+")) for line in lines if line != ""]

dial = 50
zeros = 0

for line in lines_as_numbers:
    dial = (dial + line) % 100
    if dial == 0:
        zeros += 1

print(zeros)