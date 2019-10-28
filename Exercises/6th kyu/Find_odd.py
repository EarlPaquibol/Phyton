# def find_it(seq):
#     new = []
#     for index, value in enumerate(seq):
#         if seq.count(value)%2 != 0:
#             new += [seq.count(value)]
#     a = max(new)
#     for i,e in enumerate(seq):
#         if seq.count(e) == a:
#             a = seq[i]
#             print('retard')
#             return a

def find_it(seq):
    odd = [seq.count(e) for e in seq if seq.count(e)%2 != 0]
    for i,e in enumerate(seq):
        if seq.count(e) == max(odd):
            n = seq[i]
            return n

print(find_it([3,3,3,3,4,4,4,4,4]))


