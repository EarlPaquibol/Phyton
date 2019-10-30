pairs = {'s': 1, 'n': -1, 'e': 2, 'w': -2}
def isValidWalk(walk):
    if len(walk) != 10:
        return False
    total = 0
    for e in walk:
        total += pairs[e]
    return total == 0




print(isValidWalk(['s', 'n', 's', 'n', 'e', 'w', 'w', 'w', 'w', 'w']))


# pairs = {'s': 1, 'n': -1, 'e': 2, 'w': -2}
# for x in pairs:
#     print(pairs[x])

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

