#fonctions
def inverse(n):
    m = str(n)
    p = " "
    q = len(m)
    for i in range(q):
        p = p + str(q - (i+1) )
    r = int( p )
    return r

def pal(n):
    a = True
    if n != inverse(n):
        a = False
    return a
    
def Lych(n):
    a = True
    i = 0
    while i <= 50 :
        i = i + 1
        n = n + inverse(n)
        if pal(n):
            a = False
    return a
    
#tests

def solve():
    i = 0
    for k in range(10000):
        if Lych(k):
            i = i + 1
    return i

assert(Lych(349) == False)
assert(pal(7337))
assert(Lych(4994))

print solve()
