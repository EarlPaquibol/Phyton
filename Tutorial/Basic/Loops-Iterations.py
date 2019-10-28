nums = [1, 2, 3, 4, 5]

for e in nums:
    if e == 3:
        print('Found it!')
        break
    print(e)

for e in nums:
    if e == 3:
        print('Found it!')
        continue                #skips to the next iteration
    print(e)


for i in range(1, 11):
    print(i)

x = 0

while x < 10:
    print(x)
    x += 1

# fruits = ['apple', 'banana', 'orange']
# x = 0
# for fruit in range(len(fruits)):
#     print(fruits[x])
#     x += 1
