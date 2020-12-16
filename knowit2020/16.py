from cachetools import cached

@cached(cache={})
def divisors(n):
    divs = set(1, n)
    
    for x in range(2, n/2):
        divs |= divisors(x)
        
    return divs
    
print(divisors(12))
