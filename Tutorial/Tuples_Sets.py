### tuple works by replacing list [] with ()
### tuple meaning immutable cannot be mutated/modified

list_one = (1, 2, 3)
print(list_one)


### sets
### sets do not allow duplicates, print out at any order, uses {}

set_one = {'Math', 'Physics'}
set_two = {'Math', 'Physical Education'}

print(set_one.intersection(set_two))   #prints the same values
print(set_one.difference(set_two))
new_set = set_one.union(set_two)
print(new_set)


###declaring empty list
empty_list = []
empty_list = list()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()

#empty set
empty_set = set()
empty_set = {}  ###>> this creates a disctionary not a setb
