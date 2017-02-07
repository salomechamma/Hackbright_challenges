"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    comb = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    count = len(hex_in) - 1
    summ = 0
    for i in range(len(hex_in)):
        if comb.get(hex_in[i],None):
            number = comb[hex_in[i]]
        else:
            number = int(hex_in[i])
        summ +=number * (16**count)
        count-=1
    return summ






if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
