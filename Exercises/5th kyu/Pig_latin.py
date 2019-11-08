def pig_it(text):
    text = text.split (' ')
    new = []
    bruh = []
    for word in text:
        if word not in ('!@#$%^&*()'):
            new.append(word[1:] + word[0] + 'ay')
        else:
            bruh.append(word)
            bruh.append(' ')
    bruh = ''.join(nigga)
    new = ' '.join(new)
    text = f'{new}{nigga}'
    return text




def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

