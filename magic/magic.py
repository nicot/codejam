fname = "a.in"
with open(fname) as f:
    lines = f.readlines()

size = int(lines.pop(0))
count = 1
while count <= size:
    firstrow = int(lines[0])
    first = lines[1:5]
    secondrow = int(lines[5])
    second = lines[5:9]

    first = lines[firstrow].rstrip().split(" ")
    second = lines[secondrow+5].rstrip().split(" ")
    
    cards = []
    for column in first:
        if column in second:
            cards.append(column)

    print("Case #" + str(count) + ": ", end = "")
    if len(cards) == 1:
        print(cards[0])
    elif len(cards) == 0:
        print("Volunteer cheated!")
    elif len(cards) > 1:
        print("Bad magician!")

    lines = lines[10:]
    count += 1
