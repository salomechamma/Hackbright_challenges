"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    if len(w1)-len(w2)>1:
        return False
    one_away = False
    i,j = 0,0
    while i<len(w1) and j<len(w2):
        if w1[i] == w2[j] or (not one_away and len(w1)==len(w2)):
            if w1[i] != w2[j]:
                one_away = True
            i+=1
            j+=1
        elif w1[i] != w2[j] and not one_away:
            one_away = True
            if len(w1)>len(w2):
                i=i+1
            elif len(w1)<len(w2):
                j =j+1
        elif w1[i] != w2[j] and one_away:
            return False
       
    return True


    # if len(w1)-len(w2)>1:
    #     return False
    # one_away = False
    # i,j = 0,0
    # while i<len(w1) and j<len(w2):
    #     if w1[i] != w2[j] and not one_away:
    #         one_away = True
    #         if len(w1)>len(w2):
    #             i=i+1
    #         elif len(w1)<len(w2):
    #             j =j+1
    #         else:
    #             i = i+1
    #             j = j+1
    #     elif w1[i] != w2[j] and one_away:
    #         return False
    #     elif w1[i] == w2[j]:
    #         i+=1
    #         j+=1
    # return True



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
