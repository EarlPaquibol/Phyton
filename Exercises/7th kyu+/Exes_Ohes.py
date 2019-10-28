# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.


# def xo(s):
#     x = 0
#     o = 0
#     for e in s:
#         if e == 'x':
#             x += 1
#         elif e == 'o':
#             o += 1
#     if x == o:
#         return True
#     else:
#         return False


# print(xo('xoxoxoxo;lkjashddsakhjdsaox'))

# def xoo(s):
#     s = list(s.lower())
#     return s.count('x') == s.count('o')


# print(xoo('xoxoxXosakjdhsakjoOOxxkjlashdkhasdjas'))


def xo(s):
    return list(s.lower()).count('x') == list(s.lower()).count('o')  ##Oct 26, 2019 4am. I became a oneliner

##THERE WAS NO NEED TO CONVERT TO LIST!!!
def xo(s):
    return s.lower().count('x') == s.lower().count('o')

print(xo('xoxoxoxo;lkjashddsakhjdsaox'))





