import time

start_time = time.time()

# First, let's read the input data from the file named 'input'.
# Assuming the structure of the input file is similar to the provided example.

def is_adjacent_to_symbol(schematic, x, y):
    """
    Check if the cell at (x, y) in the schematic is adjacent to a symbol.
    A symbol is any character that is not a number or a period.
    """
    rows = len(schematic)
    cols = len(schematic[0])

    # Directions to check adjacent cells (8 directions)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if not schematic[nx][ny].isdigit() and schematic[nx][ny] != '.':
                return True
    return False

def sum_part_numbers(filename):
    """
    Read the engine schematic from the file and sum all the part numbers.
    """
    with open(filename, 'r') as file:
        schematic = [line.strip() for line in file.readlines()]

    total_sum = 0

    for i, row in enumerate(schematic):
        number = ""
        for j, char in enumerate(row):
            if char.isdigit():
                number += char  # Build the number
                # Check if this is the end of the number and if it's adjacent to a symbol
                if j == len(row) - 1 or not row[j + 1].isdigit():
                    if is_adjacent_to_symbol(schematic, i, j):
                        total_sum += int(number)
                    number = ""  # Reset for the next number

    return total_sum

# Now, call the function with this test file
print(sum_part_numbers("input"))




for i in range(1000):
    sum_part_numbers("input")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")