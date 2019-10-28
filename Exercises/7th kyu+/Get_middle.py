def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        a = int(length/2 - 1)
        return s[a:length-a]
    else:
        a = length//2 + 1
        return s[a-1]

