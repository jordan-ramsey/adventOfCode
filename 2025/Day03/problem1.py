maxSum = 0
with open("input.txt", "r") as file:
    for line in file:
        digits = [int(item) for item in line.strip()]
        l, r = 0, 1
        for i in range(1, len(digits)):
            if digits[i] > digits[l] and i < len(digits) - 1:
                l = i
                r = i + 1
            else:
                if digits[i] > digits[r]:
                    r = i
        maxSum += digits[l] * 10 + digits[r]

print(maxSum)

