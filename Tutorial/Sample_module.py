print('Imported sample module...')

test = 'test string'
def find_index(to_search, target):
    #find index of the target
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
