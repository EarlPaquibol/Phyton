courses = ["History", "Math", "Physics", "Compsci"]
print(len(courses))  #prints length of lists

print(courses[-1])  #prints the last value in the list
print(courses[:2])  #prints first to second value

courses.append("Art")
print(courses)

popped = courses.pop()       #removes art or last value from the list
courses.insert(0, "Art")
print(popped)

courses_2 = ["Education"]
courses.extend(courses_2)    #extend for each item, append or insert for list to list
print(courses)

courses.remove('Math')
courses.remove('Education')
courses.remove('Art')
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
num = [1,5,3,8,2]
num.sort(reverse=True)   #sort can take an arguement, reverse
print(num)
###     use sorted when you need to keep the original value
num_sort = sorted(num)

###
print(min(num))
print(max(num))
print(sum(num))

courses = ["History", "Math", "Physics", "Compsci"]
print(courses.index('Compsci'))
print('Art' in courses)
print('Math' in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)


a = list(range(1,100))
