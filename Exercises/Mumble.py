# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

# def accum(s):
#     total = ""
#     word = ""
#     num = 1
#     for e in s:
#         for i in range(0,num):
#             word += e
#         num += 1
#         total += word[0].upper() + word[0:-1].lower()  + '-'
#         word = ""
#     return total[:-1]

# print(accum('NANI'))


##possible solutions

# def accum(s):
#     total = ""
#     i = 0
#     for letter in s:
#         total += letter.upper() + letter.lower()*i + '-'
#         i += 1
#     print(total[:-1])




def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum('abc'))
