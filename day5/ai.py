import time

start_time = time.time()



def convert_number(number, conversion_map):
    """
    Convert a single number using the provided conversion map.
    """
    for dest_start, source_start, length in conversion_map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number  # If the number is not in the map, it maps to itself


def convert_seeds_through_categories(seeds, maps):
    """
    Convert a list of seed numbers through a series of category maps.
    """
    for conversion_map in maps:
        seeds = [convert_number(seed, conversion_map) for seed in seeds]
        # print(seeds)
    return seeds


def find_lowest_location_number(seeds, maps):
    """
    Find the lowest location number that corresponds to any of the initial seed numbers.
    """
    final_numbers = convert_seeds_through_categories(seeds, maps)
    return min(final_numbers)


def parse_input_file(file_path):
    """
    Parse the input file to extract seeds and category maps, fixing the issue with an empty list.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    seeds = []
    maps = []
    current_map = []
    first_header = True

    # Parse each line
    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        if ':' in line:  # Header line
            if first_header:  # First header with seeds
                seeds = [int(x) for x in line.split(':')[1].split()]
                first_header = False
            else:  # Subsequent headers for maps
                if current_map:
                    maps.append(current_map)
                current_map = []
        else:  # Data line
            parts = [int(x) for x in line.split()]
            current_map.append(tuple(parts))

    # Add the last map
    if current_map:
        maps.append(current_map)

    return seeds, maps


# Parse the input file
seeds, maps = parse_input_file('input')

# Find the lowest location number
# lowest_location_number = find_lowest_location_number(seeds, maps)
# print(lowest_location_number)


# print(seeds)
# print(maps)

# print(find_lowest_location_number(seeds, maps))
for i in range(1000):
    find_lowest_location_number(seeds, maps)

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")