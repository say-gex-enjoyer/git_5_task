import math
def C(n, k):
    return math.factorial(n) / (math.factorial(k) * (math.factorial(n-k)))

p = 5.3
summ = 0
for i in range(1, 21):
    P = (p ** i * 2.7182848281 ** (-p)) / (math.factorial(i))
    
    summ += P
    print(i, P, summ)
print(summ)
