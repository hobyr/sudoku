import random

# generate 9x9 grid
grid = []
gridSize = 9
for i in range(gridSize):
    grid.append([None]*gridSize)

print(grid)

i = 0   # iterator for the grid generation
while grid[5][8] is None:
    # generate random array of numbers between 1 and 9
    nums = [n for n in range(1,10)]
    random.shuffle(nums)

    # add the first row to the grid
    if i == 0:
        grid[i] = nums
        continue

    # check compatibility of new row with the columns
    if num in ([grid[0][col], grid[1][col], grid[2][col],
              grid[3][col], grid[4][col], grid[5][col],
              grid[6][col], grid[7][col], grid[8][col]]):
        continue

    # check it doesn't exist in the corresponding square
    if row < 3:
        if col < 3:
            arr = grid[0][0:3] + grid[1][0:3] + grid[2][0:3]
            if num in arr:
                continue
        elif col >=3 and col < 6:
            arr = grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
            if num in arr:
                continue
        else:
            arr = grid[0][6:9] + grid[1][6:9] + grid[2][6:9]
            if num in arr:
                continue
    if row >= 3 and row < 6:
        if col < 3:
            arr = grid[3][0:3] + grid[4][0:3] + grid[5][0:3]
            if num in arr:
                continue
        elif col >=3 and col < 6:
            arr = grid[3][3:6] + grid[4][3:6] + grid[5][3:6]
            if num in arr:
                continue
        else:
            arr = grid[3][6:9] + grid[4][6:9] + grid[5][6:9]
            if num in arr:
                continue
    else:
        if col < 3:
            arr = grid[6][0:3] + grid[7][0:3] + grid[8][0:3]
            if num in arr:
                continue
        elif col >=3 and col < 6:
            arr = grid[6][3:6] + grid[7][3:6] + grid[8][3:6]
            if num in arr:
                continue
        else:
            arr = grid[6][6:9] + grid[7][6:9] + grid[8][6:9]
            if num in arr:
                continue

    # insert random number
    grid[row][col] = num
    i += 1
    nums.pop(val)
    breakpoint()
    # ensure at generation that they can't be found in the same row nor column

for i in range(gridSize):
    print(grid[i])
