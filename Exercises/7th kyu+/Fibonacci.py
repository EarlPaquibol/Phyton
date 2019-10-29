def fibo(num):
    n1 = 0
    n2 = 1
    counter = 0
    fib_list = []
    while counter < num:
        nth = n1 +n2
        n1 = n2
        n2 = nth
        fib_list.append(n1)
        counter+=1
    return fib_list




print(fibo(100))
