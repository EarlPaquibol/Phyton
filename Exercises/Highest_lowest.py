# def high_and_low(numbers):
#     # numbers = numbers.split(' ')
#     numbers = list(map(int, numbers.split(' ')))
#     numbers.sort()
#     numbers = "{}".format(numbers[-1]) + " {}".format(numbers[0])
#     return numbers



# print(high_and_low('5 3 2 221 321'))



def high_and_low(numbers):
    numbers = list(map(int, numbers.split(' ')))
    return f'{max(numbers)}' + f' {min(numbers)}'

print(high_and_low('5 3 2 221 321'))
