freshIngredientsCount = 0

with open("input.txt", "r") as file:
    rangesInput = file.read().split("\n\n")[0]
    ranges = [tuple(map(int, r.split("-"))) for r in rangesInput.split()]
    ranges.sort(key=lambda x: x[0])

    current = 0
    for (start, end) in ranges:
        if current < start:
            freshIngredientsCount += (end - start) + 1
            current = end
        elif current < end:
            freshIngredientsCount += end - current
            current = end

print(freshIngredientsCount)
