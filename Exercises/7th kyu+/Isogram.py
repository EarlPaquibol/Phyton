# def is_isogram(string):
#     for e in string.lower():
#         if string.lower().count(e) > 1:
#             return False
#     return True


def is_isogram(string):
    return len(string) == len(set(string.lower()))



print(is_isogram('qwerty'))



string = 'qwertyyq'
q = set(string)
print(q)
