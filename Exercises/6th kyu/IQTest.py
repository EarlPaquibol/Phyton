def iq_test(numbers):
    numbers = [int(e) for e in numbers.split(' ')]
    odd = [x for x in numbers if x%2 != 0]
    even = [x for x in numbers if x%2 == 0]
    return numbers.index(even[0])+1 if sum(odd) > sum(even) else numbers.index(odd[0])+1



print(iq_test("2 4 7 8 10"))


# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]

#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

#https://www.codewars.com/kata/552c028c030765286c00007d/solutions/python
