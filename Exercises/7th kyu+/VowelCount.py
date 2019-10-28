def getCount(inputStr):
    return inputStr.count('a') + inputStr.count('e') + inputStr.count('i') + inputStr.count('o') + inputStr.count('u')


print(getCount('aeioudasjhgsajgdkjhsdahkjgadsfghkjadfs'))


def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels += 1
    return num_vowels

print(getCount('aeioudasjhgsajgdkjhsdahkjgadsfghkjadfs'))
