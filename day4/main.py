import time

start_time = time.time()


def main():
    cards = {}
    with open("input", 'r') as file:
        i = 1
        for row in file:
            row = row.replace('\n', '').split(': ')[1]
            wining = row.split(' | ')[0].strip().replace('  ', ' ').split(' ')
            numbers = row.split(' | ')[1].strip().replace('  ', ' ').split(' ')

            matcing = len(set(wining) & set(numbers))

            cards[i] = {
                "row": i,
                "cards": 1,
                "winnings": matcing
            }
            i += 1

    total = 0
    for key, val in cards.items():
        if val["winnings"] > 0:
            add_cards(val, key, cards)


    for key, val in cards.items():
        total += val['cards']

    return total


def add_cards(val, key, cards):
    for i in range(val["winnings"]):
        cards[key+i+1]['cards'] += val['cards']


# print(main())
for i in range(1000):
    main()

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
