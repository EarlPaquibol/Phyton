# def find_short(s):
#     length = []
#     for word in s.split(' '):
#         length += [len(word)]
#     return min(length)





def find_short(s):
    return min(len(x) for x in s.split(' '))

print(find_short("hello world a askjhdaskdhas"))
