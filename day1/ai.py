import time

start_time = time.time()

def calculate_calibration_sum(file_path):
    total_sum = 0

    # Define a dictionary to convert written numbers to digits
    number_words = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    with open(file_path, 'r') as file:
        for line in file:
            if line:  # Check if the line is not empty
                first_digit = None
                last_digit = None

                # Replace written numbers with digits
                for word in number_words:
                    line = line.replace(word, number_words[word])

                # Find the first and last digit in the modified line
                for char in line:
                    if char.isdigit():
                        first_digit = char
                        break

                for char in reversed(line):
                    if char.isdigit():
                        last_digit = char
                        break

                # If both digits are found, add their combined value to the total sum
                if first_digit is not None and last_digit is not None:
                    total_sum += int(first_digit + last_digit)

    return total_sum


for i in range(1000):
    calculate_calibration_sum("input")
print(calculate_calibration_sum("input"))

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")