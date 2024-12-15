import math
def C(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
N = 15
K = 5
k = 3
n = 7

print ((C(K,k) * C(N - K, n - k)) / C(N,n))


yb_ap = (3/5 * 3/8 * 1/2)
ap_yb = (2/5 * 5/8 * 1/2)
yb_yb = (3/5 * 5/8)
print(yb_ap, ap_yb, yb_yb, yb_ap + ap_yb + yb_yb)
