def common_string(words1, words2):
    i = 0
    j = 0
    longest_com_words = set()
    constructing = False
    common_word = ''
    while i < len(words1) and j < len(words2):
        if words1[i] == words2[j] :
            if common_word == '':
                constructing = True
            common_word += words1[i]
           

        else:
            if common_word != '':
                longest_com_words.add(common_word)
                constructing = False
                common_word = ''
        if i == len(words1) - 1:
            if constructing:
                longest_com_words.add(common_word)
                common_word = ''
                constructing = False
            i = 0
            j += 1
        else:
            if constructing:
                j+=1
            i+=1
        # print common_word
    if constructing:
        longest_com_words.add(common_word)
    max_term = ''
    for item in longest_com_words:
        if len(max_term) < len(item):
            max_term = item
    print longest_com_words
    print max_term
    print len(max_term)


# Rosetta solution/ slightly different instructions as taking all common character and assemble them in sequence
# https://rosettacode.org/wiki/Longest_common_subsequence#Python
def lcs(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)


