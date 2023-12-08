import time
import re

start_time = time.time()


def main():
    total = 0
    rows = []
    with open("input", 'r') as file:
        for row in file:
            row = row.replace('\n', '')
            row = list(row)
            rowStatus = {
                "stars": [],
                "numbers": []
            }

            number = ''
            numberIndeces = []
            row_len = len(row)
            for iChar, c in enumerate(row):
                if c.isnumeric():
                    number += c
                    numberIndeces.append(iChar)
                    if iChar == row_len - 1:
                        rowStatus["numbers"].append({
                            "indeces": numberIndeces,
                            "number": int(number)
                        })
                else:
                    try:
                        rowStatus["numbers"].append({
                            "indeces": numberIndeces,
                            "number": int(number)
                        })
                        number = ''
                        numberIndeces = []
                    except:
                        pass

                    stars = []
                    if c == "*":
                        if iChar > 0:
                            stars.append(iChar-1)
                        stars.append(iChar)
                        if iChar < row_len - 1:
                            stars.append(iChar+1)
                        rowStatus["stars"].append(stars)
            rows.append(rowStatus)
    len_rows = len(rows)
    for iRow, row in enumerate(rows):
        if row["stars"]:
            for stars in row["stars"]:
                numbers = []
                if iRow > 0:
                    asd = check(rows[iRow - 1], stars)
                    if asd:
                        numbers = numbers + asd

                asd = check(rows[iRow], stars)
                if asd:
                    numbers = numbers + asd

                if iRow < len_rows - 1:
                    asd = check(rows[iRow + 1], stars)
                    if asd:
                        numbers = numbers + asd
                if len(numbers) == 2:
                    total += numbers[0] * numbers[1]
    return total


def check(row, indeces):
    numbers = []
    for number in row["numbers"]:
        if set(indeces) & set(number["indeces"]):
            numbers.append(number["number"])

    return numbers


# print(main())
for i in range(1000):
    main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
