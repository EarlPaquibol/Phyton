def find_even_index(arr):
    arr = list(arr)
    if (sum(arr) == arr[-1]):
        return arr.index(arr[-1])
    print(arr)
    num = arr
    a = 0
    i = 0
    while a != sum(num):
        if sum(num) == 0:
            return -1
        if a == sum(arr[1:]):
            return i
        a += num[0]
        num.remove(num[0])
        i += 1
    if (sum(arr) == 0):
        return 0
    return -1


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1






print(find_even_index([10,-80,10,10,15,35,20]))





# num = [1,100,50,-51,1,1]
# print(sum(num))
# a = num[0]
# num.remove(num[0])
# print(a, sum(num))
# a += num[1]
# num.remove(num[1])
# print(a, sum(num))



