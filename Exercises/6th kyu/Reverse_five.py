def spin_words(sentence):
    sentence = sentence.split()
    new = []
    for e in sentence:
        if len(e) > 4:
            new.append(e[::-1])
        else:
            new.append(e)
    return(' '.join(new))

print(spin_words("Hello my friend"))

def spin_words(sentence):
    return(' '.join([''.join(reversed(e)) if len(e) > 4 else e for e in sentence.split()]))  ###my one lin3r

def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())


