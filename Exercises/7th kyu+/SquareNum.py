def is_square(n):
    if n < 0:
        return False
    else:
        an = int(n**(1/2))
    if an*an == n:
        return True
    else:
        return False

print(is_square(36))


# import math
# def is_square(n):
#     if n < 0:
#         return False
#     sqrt = math.sqrt(n)
#     return sqrt.is_integer()


# import math
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;
