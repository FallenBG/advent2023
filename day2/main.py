import time
import re

start_time = time.time()

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main():
    total = 0
    with open("input", 'r') as file:
        for row in file:
            row = row.replace('\n', '')
            games = row.split(': ')[1].split('; ')
            minimumColors = {
                "red": [],
                "green": [],
                "blue": []
            }
            for game in games:
                subGames = game.split(', ')
                for subGame in subGames:
                    count = int(subGame.split(' ')[0])
                    color = subGame.split(' ')[1]
                    minimumColors[color].append(count)
            for col in minimumColors:
                minimumColors[col].sort()
            total += minimumColors['red'][-1] * minimumColors['green'][-1] * minimumColors['blue'][-1]

    return total

# main()
for i in range(1000):
    main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
