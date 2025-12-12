freshIngredientsCount = 0

with open("input.txt", "r") as file:
    ranges, ingredients = file.read().split("\n\n")

    for ingredient in ingredients.split():
        for range in ranges.split():
            if int(range.split("-")[0]) <= int(ingredient) <= int(range.split("-")[1]):
                freshIngredientsCount += 1
                break

print(freshIngredientsCount)