### File objects


# f = open('test.txt', 'r')    #opens file for reading. w for writing, will overwrite. r+ for read and write. a for appending, will add.
# print(f.name)
# f.close()


# with open('test.txt', 'r') as f:   #automatically closes the text file
#     f_contents = f.read()           #read(x) wherein x is the number of characters you want to read
    # print(f_contents)
    # f_contents = f.readline()     #readlines() every line
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # for lines in f:
    #     print(lines, end='')
    #f.seek(x) wherein x will be the place where it starts to read



# with open('test2.txt', 'w') as f:
#     f.write('pogi')
#     f.seek(0)
#     f.write('earl')


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        size_to_read = 100
        rf_chunk = rf.read(size_to_read)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(size_to_read)

# for lines in rf:
#     wf.write(lines)


