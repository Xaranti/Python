import time
import functools

@functools.lru_cache(100)
def fib(n):  
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
           
    return result

start = time.time()
for i in range(1,60):
    print(i,' = ',fib(i))
stop = time.time()
print(stop-start)
print(fib.cache_info())