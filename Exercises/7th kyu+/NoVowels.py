# def disemvowel(string):
#     for e in string:
#         if ('a' == e or 'e' == e or 'i' == e or 'o' == e or 'u' == e or
#         'A' == e or 'E' == e or 'I' == e or 'O' == e or 'U' == e):
#             string = string.replace(e, '')
#     return string





# def disemvowel(string):
#     return "".join(c for c in string if c not in "aeiouAEIOU")




def disemvowel(string):
    c = ''
    for c in string:
        if c not in "aeiouAEIOU":
            c += c
    print (c)
print(disemvowel("This website is for losers LOL!"))
