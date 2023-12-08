import time

start_time = time.time()


def sum_of_valid_game_ids_from_file(file_path):
    total_power = 0

    with open(file_path, 'r') as file:
        for game in file:
            sets = game.split(': ')[1].split('; ')

            min_red, min_green, min_blue = 0, 0, 0
            for set_ in sets:
                cubes = set_.split(', ')
                red_count = sum(int(cube.split(' ')[0]) for cube in cubes if 'red' in cube)
                green_count = sum(int(cube.split(' ')[0]) for cube in cubes if 'green' in cube)
                blue_count = sum(int(cube.split(' ')[0]) for cube in cubes if 'blue' in cube)

                min_red = max(min_red, red_count)
                min_green = max(min_green, green_count)
                min_blue = max(min_blue, blue_count)

            power = min_red * min_green * min_blue
            total_power += power

    return total_power


for i in range(1000):
    sum_of_valid_game_ids_from_file("input")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")