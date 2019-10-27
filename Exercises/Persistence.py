# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.



# def persistence(num):
#     if len(str(num)) == 1:
#         return 0
#     num = [int(e) for e in str(num)]
#     digits = functools.reduce(lambda x,y:x*y, num)
#     counter = 1
#     while len(str(digits)) > 1:
#         digits = [int(e) for e in str(digits)]
#         num = functools.reduce(lambda x,y:x*y, digits)
#         digits = num
#         counter += 1
#     return counter




import functools
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = functools.reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist


print(persistence(25))







# new = []
# for e in str(total):
#     new += [int(e)]

# num = 98
# total = []
# for e in str(num):
#     total += [int(e)]

# num = [int(e) for e in str(num)]
# print(total)
