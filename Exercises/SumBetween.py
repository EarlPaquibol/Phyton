def get_sum(a,b):
    if a<b:
        return sum(range(a,b+1))
    else:
        return sum(range(b,a+1))




print(get_sum(1,0))

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))
