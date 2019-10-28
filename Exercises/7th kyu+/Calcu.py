#sample calcu program
a = 4
b = 2
operator = '+'

def add(a, b):     #functions must be declared first
    print(a+b)

def mul(a, b):
    print(a*b)

def div(a, b):
    print(a/b)

def sub(a, b):
    print(a-b)

def pow(a):
    print(a**2)

if operator == '+':
    add(a,b)
elif operator == '-':
    sub(a,b)
elif operator == '*':
    mul(a,b)
elif operator == '/':
    div(a,b)
else:
    pow(a)
