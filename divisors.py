#Create a function named divisors that takes an integer and returns an array 
# with all of the integer's divisors(except for 1 and #the number itself). 
# If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).

def divisors(n):
    nb = 0
    divisors = []
    for i in range(2,n):
        if n % i == 0:
            nb+=1
            divisors.append(i)
    if nb == 0:
        print '%s is prime'%(n)
    else:
        return divisors 



# Other solution with list comprehension
def divisors2(n):
    divisors = [i for i in range(2,n) if n % i == 0]
    if len(divisors) == 0:
        return '%s is prime'%(n)
    else:
        return divisors 