invalidSum = 0

with open("input.txt", "r") as file:
    codes = file.read().split(",")
    for code in codes:
        start, end =  code.split("-")
        for i in range(int(start), int(end) + 1, 1):
            for k in range(1, len(str(i)) // 2 + 1, 1):
                codeAsString = str(i)
                length = len(codeAsString)
                # optimization, only divide by factors
                if length % k == 0:
                    if codeAsString[0:k] * (length // k) == codeAsString:
                        invalidSum += int(codeAsString)
                        break

print(invalidSum)