import time
import re

start_time = time.time()


def convert_number(number, conversion_map):
    """
    Convert a single number using the provided conversion map.
    """
    number = int(number)
    for dest_start, source_start, length in conversion_map:
        source_start = int(source_start)
        dest_start = int(dest_start)
        length = int(length)
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number  # If the number is not in the map, it maps to itself


def convert_seeds_through_categories(seeds, maps):
    """
    Convert a list of seed numbers through a series of category maps.
    """
    for conversion_map in maps:
        seeds = [convert_number(seed, conversion_map) for seed in seeds]

    return seeds


def main():
    with open("input", 'r') as file:
        file = file.read().split('\n\n')
        seeds = file.pop(0).split(':')[1].strip().split(' ')

        maps = []
        for i, map in enumerate(file):
            maps.append(split_rows_of_numbers(file, i))

    return min(convert_seeds_through_categories(seeds, maps))


def split_rows_of_numbers(file, part):
    rows = file[part].split(':')[1].strip().split('\n')
    for i, row in enumerate(rows):
        rows[i] = tuple(row.split(' '))

    return rows


# print(main())
for i in range(1000):
    main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
