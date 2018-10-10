#Definition Fonction

def exo16(n):
    i = 0 #indice des dizaines ( ne marche pas pour n = 1 )
    
    while n/(10**i) > 1 : #calcul le nombre de chiffres du nombre)
        i = i+1
    SOMME = 0
    p = 0
    
    for j in range(i): #effectue des divisions euclidiennes
        p = n//(10**(i-j))
        SOMME = SOMME + p
        n = n - p*(10**(i-j))
    
    return SOMME + n
    
#tests
def solve():
    return exo16(2**1000)


assert solve(2**15) == 26
assert solve(32768) == 26
print solve()