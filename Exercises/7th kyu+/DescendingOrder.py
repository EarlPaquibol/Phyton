# def Descending_Order(num):
#     st = str(num)
#     my_total = []
#     # for num in st:
#     #     my_total += [int(num)]
#     my_total = [int(num) for num in st]
#     my_total.sort()
#     my_total.reverse()
#     st = str(my_total)
#     st = st[1:-1]
#     st = st.replace(', ', '')
#     num = int(st)
#     print(num)
### same funcs, just tried to make it cleaner




def Descending_Orderr(num):
    string_num = str(num)
    list_num = [int(num) for num in string_num]
    list_num.sort()
    list_num.reverse()
    st = str(list_num)
    num = int(st[1:-1].replace(', ', ''))
    return num

def Descending_Order(num):
    s = str(num)
    s = list(s)     ##no need to convert to list, sorted automatically converts a string into a list
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    print(s)
    return int(s)

def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))

Descending_Orderr(134454236546645)
Descending_Order(134454236546645)

