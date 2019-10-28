import functools

def digital_root(n):
    n = [int(e) for e in str(n)]
    while len(n) > 1:
        new = functools.reduce(lambda x,y: x+y, n)
        n = [int(e) for e in str(new)]
    return sum(n)




print(digital_root(166))


# def digital_root(n):
#   return n%9 or n and 9

#   If n % 9 != 0 return n % 9. Otherwise return n (if n == 0) or 9 (if n != 0).
