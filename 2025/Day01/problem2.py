dial = 50
zeroCount = 0

with open("input.txt", "r") as file:
    for line in file:
        direction, num = line[0], int(line[1:].strip())

        if direction == "L":
            if num >= dial:
                zeroCount += (num // 100) if dial == 0 else 1 + (num - dial) // 100
            dial = (dial - num) % 100
        elif direction == "R":
            zeroCount += (dial + num) // 100
            dial = (dial + num) % 100


print(zeroCount)