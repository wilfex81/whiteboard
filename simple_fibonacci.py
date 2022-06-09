from functools import lru_cache

#specify the max size to be cached, if not default value will be used)
@lru_cache(maxsize = 1000)
def fibonaci(n):
  if n == 1:
    return 1
  elif n==2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)
  
  for i in range(1, 1001):
    print(n, ":", fibonacci(n))
