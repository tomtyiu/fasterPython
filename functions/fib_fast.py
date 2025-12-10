import time
from functools import lru_cache

#Leverage functools.lru_cache for Repeated Calls
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
    
#timeit.timeit(my_code, number=2)
#Total time taken: 0.012247900000147638
