import time
import re

start_time = time.time()
pattern = re.compile(r'(?=(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9))')

match = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def returnInt(string):
    try:
        int(string)
        return string
    except:
        return match[string]

def main():
    total = 0
    with open("input", 'r') as file:
        for row in file:
            row = row.replace('\n', '')
            matches = pattern.findall(row)
            first = returnInt(matches[0])
            last = returnInt(matches[-1])
            total += int(first + last)

    print(total)

main()
# for i in range(1000):
#     main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
