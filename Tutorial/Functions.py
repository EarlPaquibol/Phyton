def empty_function():
    pass

def hello_func(greeting):
    return f'{greeting} function!'

a = hello_func('Hi')
print(a)

def hello_func_default(greeting, name = 'You'):
    return f'{greeting} {name}!'

a = hello_func_default('sup')
print(a)


def student_info(*args, **kwargs):
    print(args)      #prints tuples
    print(kwargs)    #prints dict

courses = ['Math', 'Biology']
info = {'name': 'Earl', 'age': 21}
student_info(*courses, **info)
