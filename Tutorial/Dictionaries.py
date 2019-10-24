#dictionary is like a class. you can create properties.

student = {'name': 'Earl', 'age': 21, 'courses': 'Software Engineering'}
print(student)


print(student['name'])         ##when key does not exist, it will return an error
print(student.get('phone', 'Key does not exist'))     ##when key does not exist, it will return none. Second argument == msg displayed when key is not found

student['phone'] = '3091209'    ##adds a key to the dictionary student
print(student.get('phone', 'Key does not exist'))

student['name'] = 'Pogi'
print(student['name'])

student.update({'name': 'Earl Pogi', 'sex': 'Male'})
print(student)

del student['age']
print(student)


Sex = student.pop('sex')
print(Sex)
print(student)

print(len(student)) #gets the number of keys
print(student.keys())  #gets the keys of the dict
print(student.values())  #gets the values of each key
print(student.items())   #gets both keys and values by pair


for key, value in student.items():
    print(key, value)
