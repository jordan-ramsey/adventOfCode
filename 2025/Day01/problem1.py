dial = 50
zeroCount = 0

with open("input.txt", "r") as file:
    for line in file:
        direction, num = line[0], int(line[1:].strip())

        if direction == "L":
            dialCount = dial - int(num)
            dial = dialCount % 100

        elif direction == "R":
            dialCount = dial + int(num)
            dial = dialCount % 100

        if dial == 0:
            zeroCount += 1

print(zeroCount)