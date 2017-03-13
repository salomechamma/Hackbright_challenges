def merge_cookie(ls1,ls2):
    ind1 = ind2 = 0
    ls_combined = []
    while ind1 < len(ls1) and ind2 < len(ls2):
        if ls1[ind1] <= ls2[ind2]:
            ls_combined.append(ls1[ind1])
            ind1 +=1
        else:
            ls_combined.append(ls2[ind2])
            ind2 +=1
    while ind1< len(ls1):
        ls_combined.append(ls1[ind1])
        ind1 +=1
    while ind2< len(ls2):
        ls_combined.append(ls2[ind2])
        ind2 +=1
    return ls_combined

merge_cookie([3, 4, 6, 10, 11, 15],[1, 5, 8, 12, 14, 19])

def merge_cookie2(ls1,ls2):
    ind1 = ind2 = 0
    ls_combined = []
    while ind1 < len(ls1) or ind2 < len(ls2):
        if ls1[ind1] <= ls2[ind2] or ind2 >= len(ls2):
            ls_combined.append(ls1[ind1])
            ind1 +=1
        elif ls1[ind1] > ls2[ind2] or ind1 >= len(ls1):
            ls_combined.append(ls2[ind2])
            ind2 +=1

    return ls_combined