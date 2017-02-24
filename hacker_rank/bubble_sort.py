n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

total_swap = 0
for i in range(n):
    nb_swap = 0
    
    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) :
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            nb_swap +=1
    
    # If no elements were swapped during a traversal, array is sorted
    if (nb_swap== 0):
        break
    total_swap += nb_swap

print 'Array is sorted in %s swaps.' %(total_swap)
print 'First Element: %s' %(a[0])
print 'Last Element: %s' %(a[-1])


    