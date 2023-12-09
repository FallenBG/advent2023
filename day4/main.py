import time

start_time = time.time()


def main():
    total = 0
    with open("input", 'r') as file:
        for row in file:
            row = row.replace('\n', '').split(': ')[1]
            wining = row.split(' | ')[0].strip().replace('  ', ' ').split(' ')
            numbers = row.split(' | ')[1].strip().replace('  ', ' ').split(' ')

            matcing = set(wining) & set(numbers)
            # print(generate_geometric_progression(len(matcing)))
            total += generate_geometric_progression(len(matcing))

    return total


def generate_geometric_progression(num_terms):
    if num_terms == 0:
        return 0
    else:
        return 1 * 2**(num_terms - 1)


# print(main())
for i in range(1000):
    main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
