def move_zeros(array):
    a = array.count(0)
    while array.count(0) > 1:
        array.remove(0)
    while array.count(0) != a:
        array.append(0)
    print(array)


move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
