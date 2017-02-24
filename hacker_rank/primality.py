# Complexity of Osqrt(n)

import math
def primality(n): 
    if n > 10 :
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                print 'Not prime'
                break
            
        else:
            print 'Prime'
    elif n <10 and n >1:
        for i in range(2,n):
            if n%i == 0:
                print 'Not prime'
                break
            
        else:
            print 'Prime'
    else:
         print 'Not prime'

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    primality(n)