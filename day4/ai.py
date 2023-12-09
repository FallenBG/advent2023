import time

start_time = time.time()

# To solve the task, I will write a Python script that reads the data from a file named "input".
# The file is expected to contain the scratchcard data in the specified format.

def calculate_points_from_file(filename):
    try:
        # Open the file and read the lines
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Extract the scratchcards and their details
        scratchcards = []
        for line in lines:
            parts = line.split(': ')
            # Ensure that the card number part is not empty and is a valid number
            # Using strip() to remove extra spaces and then split
            card_number = int(parts[0].replace('Card', '').strip())

            winning_numbers, your_numbers = parts[1].split(' | ')
            winning_numbers = set(map(int, winning_numbers.split()))

            your_numbers = set(map(int, your_numbers.split()))
            scratchcards.append((card_number, winning_numbers, your_numbers))

        # Function to calculate matches for each scratchcard
        def calculate_matches(winning_numbers, your_numbers):
            return len(winning_numbers.intersection(your_numbers))

        # Initialize the count of each card (originals)
        card_counts = {card_number: 1 for card_number, _, _ in scratchcards}

        # Process each card
        for i in range(len(scratchcards)):
            current_card, winning_numbers, your_numbers = scratchcards[i]
            matches = calculate_matches(winning_numbers, your_numbers)

            # Win copies of the next cards equal to the number of matches
            for j in range(i + 1, min(i + 1 + matches, len(scratchcards))):
                next_card, _, _ = scratchcards[j]
                card_counts[next_card] += card_counts[current_card]

        # Calculate the total number of scratchcards
        total_scratchcards = sum(card_counts.values())
        return total_scratchcards

    except FileNotFoundError:
        return "File not found."
    except ValueError as e:
        return str(e)


print(calculate_points_from_file('input'))
for i in range(1000):
    calculate_points_from_file("input")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")