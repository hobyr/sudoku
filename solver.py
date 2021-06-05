"""Sudoku solver script."""


import time


def performance(func):
    """Measure elapsed execution time in seconds."""
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f'Elapsed time: {t2-t1}s')

    return wrapper


def is_valid(grid, row, col):
    """Check if the complete sudoku grid is OK.

    :grid: Sudoku grid complete or incomplete

    """
    # Check if the number appears only once in the row
    if not check_row(grid, row, col):
        return False

    # Check if the number appears only once in the column
    if not check_column(grid, row, col):
        return False

    # Check if the number appears only once in the subgrid
    if not check_subgrid(grid, row, col):
        return False

    # If ok, go to next number

    # If all numbers are ok, return True
    return True


def check_row(grid, row, col):
    """Verify the uniqueness of the selected number in its row.

    :grid: complete sudoku grid
    :row: row of the number to be checked
    :col: column of the number to be checked

    """
    # Get the number to be checked
    num = grid[row][col]

    # Get the row to be checked
    row = grid[row]

    # Check if the number to be checked appears only once
    if row.count(num) == 1:

        # Return true if yes
        return True

    # Return false otherwise
    return False


def check_column(grid, row, col):
    """Verify the uniqueness of the selected number in its column.

    :grid: complete sudoku grid
    :row: row of the number to be checked
    :col: column of the number to be checked

    """
    # Get the number to be checked
    num = grid[row][col]

    # Get the column to be checked
    col = [grid[i][col] for i in range(9)]

    # Check if the number to be checked appears only once
    if col.count(num) == 1:

        # Return true is yes
        return True

    # Return false otherwise
    return False


def check_subgrid(grid, row, col):
    """Verify the uniqueness of the selected number in its surrounding subgrid.

    :grid: complete sudoku grid
    :row: row of the number to be checked
    :col: column of the number to be checked

    """
    # Get the number to be checked
    num = grid[row][col]

    # Get the subgrid to be checked
    i = 3 * (row // 3)
    k = 3 * (col // 3)
    subgrid = [grid[i][k:k+3], grid[i+1][k:k+3], grid[i+2][k:k+3]]
    flat_sub = [num for row in subgrid for num in row]

    # Check if the number to be checked appears only once
    if flat_sub.count(num) == 1:

        # Return true if yes
        return True

    # Return false otherwise
    return False


def zero_coordinates(grid):
    """Find the coordinates of the zeros.

    :grid: entire sudoku grid to be filled
    :returns: the coordinates of the empty cells

    """
    coord = []
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                coord.append((row, col))
    return coord


def print_grid(grid):
    """Print the grid in sudoku form."""
    for row in range(9):
        for col in range(9):
            if col % 3 == 2 and col < 8:
                print(grid[row][col], end='|')
            elif col == 8:
                print(grid[row][col])
            else:
                print(grid[row][col], end=' ')
        if row % 3 == 2 and row < 8:
            print('-----+-----+-----')


def solve_sudoku(grid, coordinates, n=0):
    """Find the Sudoku solution using a backtracking algorithm.

    :grid: Sudoku grid to be filled
    :coordinates: locations of the 0 in the grid
    :n: current location to be found

    """
    row = coordinates[n][0]
    col = coordinates[n][1]

    for num in range(1,10):
        grid[row][col] = num

        if is_valid(grid, row, col):
            if n+1 == len(coordinates):
                return True
            elif solve_sudoku(grid, coordinates, n+1):
                return True

        grid[row][col] = 0

    return False


@performance
def main():
    """Execute the program's main function."""
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 6, 7, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 3, 0, 7, 0],
        [9, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6 ,0],
        [0, 7, 0, 0, 6, 0, 0, 8, 0],
        [0, 0, 6, 5, 3, 2, 4, 9, 0],
        [3, 0, 0, 1, 0, 0, 0, 2, 8],
        [0, 0, 0, 0, 4, 0, 6, 3, 0]
    ]

    print('Input grid:')
    print_grid(grid)

    coordinates = zero_coordinates(grid)

    print('\nSolution:')
    solve_sudoku(grid, coordinates)
    print_grid(grid)
    print('')


if __name__ == "__main__":
    main()
