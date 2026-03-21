from math import log10
import math 
def karatsuba(n,m):
    
    if n<10 or m<10:
        return n*m
    
    k = max(len(str(n)),len(str(m)))
    
    k_2 = int(math.ceil(k/2.0))
    
    k = k if k % 2 == 0 else k+1
    
    a,b = divmod(n,10**k_2)
    c,d = divmod(m,10**k_2)
    
    
    p = karatsuba(a,c)
    q = karatsuba(b,d)
    r = karatsuba((a+b),(c+d))
    
    return p*10**k + (r-p-q)*10**k_2 + q







print(karatsuba(1024,2034))