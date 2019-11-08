def scramble(s1, s2):
    if len(s2) > len(s1):
        return False
    return len([char for char in s2 if char in s1]) == len(s2)

print(scramble('cedewaraaossoqqyt', 'codewars'))




# def scramble(s1, s2):
#     for char in s2:
#         if char in s1:
#             s1 = s1.replace(char, '', 1)
#         else:
#             return False
#     return True


# def scramble(s1, s2):
#     for char in s2:
#         if char not in s1:
#             return False
#     return True

# print(scramble('katas', 'steak'))


