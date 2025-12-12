numOfValidCells = 0

with open("input.txt", "r") as file:
    cells = [list(line.strip()) for line in file]

for i in range(len(cells)):
    for j in range(len(cells[i])):
        if cells[i][j] != '@':
            continue
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      ( 0, -1),         ( 0, 1),
                      ( 1, -1), ( 1, 0), ( 1, 1)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(cells) and 0 <= nj < len(cells[i]) and cells[ni][nj] == '@':
                count += 1
        if count < 4:
            numOfValidCells += 1

print(numOfValidCells)
