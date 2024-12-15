import math
def C(n, k):
    return math.factorial(n) / (math.factorial(k) * (math.factorial(n-k)))



n = 4500
p = 0.59
q = 1 - p

lambd = n * p
P = 0
P_1 = lambd**2600 * 2.718284 ** (-lambd) / (math.factorial(2600))


print(1 - P)
print(P_1)

#p = 0.59
#np = 2655
#npp = 1566.45
#npq = 1088.55


# 0.001
# 0.2149
#0.0025
print(0.2149 + 0.0025, 0.2149 - 0.0025)

# FI_1 (B - np) / (sqrt(npq))
# FI_2 (A - np) / (sqrt(npq))
#A = 2604
#B = 2699

# FI_1 = 44 / sqrt(1566.45)
# FI_2 = 2 / sqrt(3.99)

#FI_1 = 0.3669
#FI_2 = 0.4013


#P (6 <= Sn <= 100) = FI_1 - FI_2 = 0.1583
print(1 / (p * q * math.sqrt(n)))
