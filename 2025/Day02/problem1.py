invalidSum = 0

with open("input.txt", "r") as file:
    codes = file.read().split(",")
    for code in codes:
        start, end =  code.split("-")
        for i in range(int(start), int(end) + 1, 1):
            if len(str(i)) % 2 == 0:
                if str(i)[0: len(str(i))//2] == str(i)[len(str(i))//2:]:
                    invalidSum += i

print(invalidSum)