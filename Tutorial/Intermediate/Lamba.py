###filter, map, reduce


import functools
sample = [1, 2, 3, 4, 5, 6]
x = list(filter(lambda x: (x%2==0), sample))
y = list(map(lambda x: x*x, sample))
z = functools.reduce(lambda x, y: x+y, sample)
print(x)
print(y)
print(z)
