def getMaxDigits(digits, k):
    maxDigits = [digits[0]]
    for i in range(1, len(digits)):
        for j in range(len(maxDigits)):
            if digits[i] > maxDigits[j] and (len(digits) - i) >= k - j:
                maxDigits[j] = digits[i]
                maxDigits = maxDigits[0 : j + 1]
                break
        else:  # No break occurred - no replacement was made
            if len(maxDigits) < k:
                maxDigits.append(digits[i])
    return int(''.join(str(d) for d in maxDigits))

maxSum = 0
k = 12
with open("input.txt", "r") as file:
    for line in file:
        digits = [int(item) for item in line.strip()]
        maxDigits = getMaxDigits(digits, k)
        maxSum += maxDigits
print(maxSum)