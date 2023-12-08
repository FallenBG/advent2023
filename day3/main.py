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
                "symbols": [],
                "numbers": []
            }

            number = ''
            numberIndeces = []
            row_len = len(row)
            for iChar, c in enumerate(row):
                if c.isnumeric():
                    number += c
                    numberIndeces.append(str(iChar))
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

                    if c != '.':
                        if iChar > 0:
                            rowStatus["symbols"].append(iChar-1)
                        rowStatus["symbols"].append(iChar)
                        if iChar < row_len - 1:
                            rowStatus["symbols"].append(iChar+1)
            rowStatus["symbols"] = set(rowStatus["symbols"])
            rows.append(rowStatus)
    len_rows = len(rows)

    for iRow, row in enumerate(rows):
        prev_set = set({})
        next_set = set({})
        if iRow > 0:
            prev_set = rows[iRow-1]["symbols"]
        if iRow < len_rows - 1:
            next_set = rows[iRow+1]["symbols"]

        merged_set = prev_set | row["symbols"] | next_set
        sorted_list = sorted(merged_set)

        for numbers in row["numbers"]:
            for i in sorted_list:
                if str(i) in numbers["indeces"]:
                    total += numbers["number"]
                    break

    return total


print(main())
# for i in range(1000):
#     main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
