# def find_outlier(integers):
#     odd = 0
#     even = 0
#     for e in integers:
#         if e%2 == 0:
#             even += 1
#         else:
#             odd += 1
#         if even > 1:
#             for e in integers:
#                 if e%2 != 0:
#                     return e
#         elif odd > 1:
#             for e in integers:
#                 if e%2 == 0:
#                     return e

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]



print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
