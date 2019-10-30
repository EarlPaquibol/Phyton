def dirReduc(arr):
    if len(arr) == 0:
        return arr
    dup = True
    i = 0
    while dup == True:
        if len(arr)-1 == i:
            dup = False
        elif len(arr) == 0:
            dup = False
        elif arr[i] == 'NORTH' and arr[i+1] == 'SOUTH':
            arr.remove('NORTH')
            arr.remove('SOUTH')
            i = 0
        elif arr[i] == 'EAST' and arr[i+1] == 'WEST':
            arr.remove('EAST')
            arr.remove('WEST')
            i = 0
        elif arr[i] == 'SOUTH' and arr[i+1] == 'NORTH':
            arr.remove('SOUTH')
            arr.remove('NORTH')
            i = 0
        elif arr[i] == 'WEST' and arr[i+1] == 'EAST':
            arr.remove('EAST')
            arr.remove('WEST')
            i = 0
        else:
            i += 1
    return arr


print(dirReduc(["NORTH", "SOUTH"]))



    # for i,e in enumerate(arr):
    #     if e == 'NORTH' and arr[i+1] == 'SOUTH':
    #         arr.remove('NORTH')
    #         arr.remove('SOUTH')
    #     elif e == 'EAST' and arr[i+1] == 'WEST':
    #         arr.remove('EAST')
    #         arr.remove('WEST')
    #     elif e == 'SOUTH' and arr[i+1] == 'NORTH':
    #         arr.remove('SOUTH')
    #         arr.remove('NORTH')
    #     elif e == 'WEST' and arr[i+1] == 'EAST':
    #         arr.remove('EAST')
    #         arr.remove('WEST')


