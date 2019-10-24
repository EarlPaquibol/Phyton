# King Arthur and his knights are having a New Years party. Last year Lancelot was jealous of Arthur,
# because Arthur had a date and Lancelot did not, and they started a duel.
# To prevent this from happening again, Arthur wants to make
# sure that there are at least as many women as men at this year's party. He gave you a list of integers of all the party goers.
# Arthur needs you to return true if he needs to invite more women or false if he is all set.

def invite_more_women(attendees):
    men = 0
    women = 0
    for sex in attendees:
        if sex == -1:
            women += 1
        else:
            men += 1
    if men > women:
        return True
    else:
        return False

print(invite_more_women([1, 1, 1]))


def invite_more_women(attendees):
    return sum(attendees) > 0                                   #ONELINER

print(invite_more_women([1, 1, 1]))
