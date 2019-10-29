def duplicate_count(text):
    text = text.lower()
    counter = 0
    for e in text:
        if text.count(e) > 1:
            text = text.replace(e, '')
            counter += 1
    return counter

print(duplicate_count('abcbc'))


def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
