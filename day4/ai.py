import time

start_time = time.time()

# To solve the task, I will write a Python script that reads the data from a file named "input".
# The file is expected to contain the scratchcard data in the specified format.

def calculate_points_from_file(filename):
    try:
        # Open the file and read the lines
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Function to calculate points for each scratchcard
        def calculate_points(scratchcard):
            # Extract the part after the colon and split the winning numbers and the numbers you have
            winning_numbers, your_numbers = scratchcard.split(': ')[1].split(' | ')
            winning_numbers = set(map(int, winning_numbers.split()))
            your_numbers = set(map(int, your_numbers.split()))

            # Count the matches
            matches = winning_numbers.intersection(your_numbers)
            if len(matches) == 0:
                return 0
            else:
                # Calculate the points
                return 2 ** (len(matches) - 1)

        # Calculate the total points
        total_points = sum(calculate_points(card) for card in lines)
        return total_points

    except FileNotFoundError:
        return "File not found."


# print(calculate_points_from_file('input'))
for i in range(1000):
    calculate_points_from_file("input")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")