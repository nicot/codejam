from collections import deque
import copy
with open('d.in') as f:
    lines = deque(f.readlines())

size = lines.popleft()
count = 1
while lines:
    trash = lines.popleft()
    nblocks = deque(sorted(lines.popleft().rstrip().split(" ")))
    kblocks = deque(sorted(lines.popleft().rstrip().split(" ")))
    kfairscore = 0
    nfairscore = 0
    nscore = 0
    kscore = 0

    nfairs = copy.deepcopy(nblocks)
    kfairs = copy.deepcopy(kblocks)
    while nfairs:
        nfair = nfairs.pop()
        if kfairs[len(kfairs)-1] > nfair:
            kfairs.popleft()
            kfairscore += 1
        else:
            while kfairs[i] < nfair:
                i += 1
            kfairs.remove(kfairs[i])
            nfairscore += 1

    while nblocks:
        # If ken has a bigger block than I do, say I'm using a kenblock minus epsilon, and really trash my worst one.
        if kblocks[len(kblocks)-1] > nblocks[len(nblocks)-1]:
            nblocks.popleft()
            kblocks.pop()
            kscore += 1
        # If I have a bigger block than ken, ken will trash his worst one.
        # Therefore, I just have to use the only one I have better than ken's.
        else:
            kblock = kblocks.popleft()
            i = 0
            while nblocks[i] < kblock:
                i += 1
            nblocks.remove(nblocks[i])
            nscore += 1

    print('Case #' + str(count) + ': ' + str(nscore) + ' ' + str(nfairscore))
    count += 1
    nblocks.clear()
    kblocks.clear()
