def countBits(n):
    binary = []
    while n > 0:
        if n%2 == 0:
            binary.append(0)
            n = n/2
        elif n%2 != 0:
            n -= 1
            n = n/2
            binary.append(1)
    return sum(binary)


# def countBits(n):
#     return bin(n).count("1")

countBits(1234)
