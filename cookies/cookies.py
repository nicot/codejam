with open('b.in') as f:
    lines = f.readlines()

size = int(lines.pop(0))
lines.reverse()
count = 1

while lines:
    cpm = 2
    cost, benefit, maxi = map(float, lines.pop().rstrip().split(" "))
    time = 0

    while cost/cpm + maxi/(benefit+cpm) < maxi/cpm:
        time += cost/cpm
        cpm += benefit

    time += maxi/cpm

    print('Case #' + str(count) + ': ' + str(time))
    count += 1
