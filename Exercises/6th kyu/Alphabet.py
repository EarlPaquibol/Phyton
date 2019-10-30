import string
alphabet = dict.fromkeys(string.ascii_lowercase)
i = 1
for x in alphabet:
    alphabet[x] = str(i)
    i += 1


# sentence = "The sunset sets at twelve o' clock."
# sentence = list(sentence.lower().split(' '))
# new = []
# for word in sentence:
#     for char in word:
#         if not char in d:
#             break
#         new.append(d[char])

# print(new)

def alphabet_position(text):
    text = list(text.lower().split(' '))
    num = []
    for word in text:
        for char in word:
            if not char in alphabet:
                break
            num.append(alphabet[char])
    num = ' '.join(num)
    return num

alphabet_position("The sunset sets at twelve o' clock.")
