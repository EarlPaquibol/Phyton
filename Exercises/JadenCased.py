# string = 'hello hello world'
# string = string.split()
# for e in string:
#     e.capitalize()
# return ''.join(e.capitalize() for e in string.split())



# def Jaden_casing(string):
#     string = string.split()
#     for e in string:
#         if e[0].islower() == True:
#             return False
#     return True


# print(Jaden_casing('Hello World Wigga'))

# def toJadenCase(string):
#     string = string.split()
#     for i, e in enumerate(string):
#         string[i] = e[0].upper() + e[1:]
#     return ' '.join(string)



# print(toJadenCase('hello world wigga'))


# def toJadenCase(string):
#     s = []
#     for e in string.split():
#         s += e[0].upper() + e[1:] + ' '
#     return ''.join(s[:-1])

# print(toJadenCase('hello world wigga'))





def toJadenCase(string):
    return ' '.join(e.capitalize() for e in string.split())

print(toJadenCase('hello world wigga'))


