# def duplicate_encode(word):
#     hello = []
#     for e in word.lower():
#         if word.lower().count(e) > 1:
#             hello.append(')')
#         else:
#             hello.append('(')
#     return ''.join(hello)

def duplicate_encode(word):
    return ''.join([')' if word.lower().count(e) > 1 else '(' for e in word.lower()])    ###ey another one liner from me

print(duplicate_encode("Receder"))

