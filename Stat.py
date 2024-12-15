from decimal import *
import math
getcontext().prec = 999999999999999999
def smartFact (n,k):
    res = 1
    for i in range(k - 1, n):
        res*= i
    return res

def CSmart(n, k):
    return smartFact(n,k) / (math.factorial(n-k))

def C(n,k):
    return fact(n) / (fact(k) * fact(n - k))

def fact(n):
    return math.factorial(n)

n = 4500
p = 0.59
q = 1 - p
P = 0


for i in range (2604,2700):
    P += Decimal(C(4500, i)) * Decimal(pow(p,i)) * Decimal(pow(q,2699-i))
    print(i, P, Decimal(p**i), Decimal(pow(p,i)))

print("P = ", P)
print(1 - P)




#for i in range (2604, 2700):
#    print("fact(4500) / (fact({}) * fact(4500 - {})) * 0.59^{} * 0.41^(4500-{}) +".format(i,i,i,i))

#for i in range (2604, 2700):
#    print("4500! / {}! * (4500 - {})) * 0.59^{} * 0.41^(4500-{}) +".format(i,i,i,i))
