#If we list all the natural numbers below 10 that are multiples of
#3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

def solution(number):
    total = 0
    for e in list(range(1,number)):
        if e%3 == 0 or e%5 == 0:
            total += e
    return total
### there was no need to create a list

print(solution(10))

for e in range(10):
    print(e)
