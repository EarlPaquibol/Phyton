# def square_digits(num):
#     num = str(num)
#     num = list(num)
#     new_list = []
#     for e in num:
#         new_list += [int(e)]
#     squared_list = []
#     for i in new_list:
#         squared_list += [i*i]
#     again = []
#     for x in squared_list:
#         again += [str(x)]
#     again = ''.join(again)
#     return int(again)



def square_digitss(num):
    return int(''.join(str(x) for x in [i*i for i in [int(e) for e in list(str(num))]]))

print(square_digitss(9119))

#good answer in kata
# def square_digits(num):
#     num = str(num)
#     ans = ''
#     for i in num:
#         ans += str(int(i)**2)
#     return int(ans)

def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))
print(square_digits(9119))
