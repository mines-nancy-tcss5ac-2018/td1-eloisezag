#fonctions
def score(w):
    score = 0
    n = len(w)
    for i in range(1, n-1):
        score = score + ord( w[i] ) - ord['A'] + 1
    return score

def trier(f):
    Liste = f.split(',')
    Liste.sort()
    return Liste
  
#tests
def solve():
    f = open("p022_names.txt", "r")
    Liste = trier(f.read())
    total = 0
    n = len(Liste)
    for i in range(n):
        total = total + score(Liste[i])*(i+1)
    return total


assert(score("COLIN") == 53
print solve()