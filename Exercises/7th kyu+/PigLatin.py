#move the first letter of the word to the last and add ay

add = "ay"
word = "EarlP"
temp_firstletter = (word[0])
pig_latin = word[1:] + temp_firstletter + add
print(pig_latin)

#sentence
#define things first
def pigLatin(string_):
    new_ = string_.split(" ", -1)
    print(new_)
    x = 0
    total = ""
    delim = " "
    for e in new_:
        temp_firstletter = (new_[0+x][0])
        pig_latin = new_[0+x][1:] + temp_firstletter + add
        total += pig_latin + delim
        x += 1
    return total



sentence = "Dave is retarded"
print(pigLatin(sentence))
