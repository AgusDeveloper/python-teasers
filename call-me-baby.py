from functools import wraps

def metrics(fn):
  ncalls = 0
  name = fn.__name__

  @wraps(fn)
  def wrapper(*args, **kw):
      nonlocal ncalls
      ncalls += 1
      print(f'{name} called {ncalls} times')

  return wrapper

@metrics
def inc(n):
  return n + 1

inc(3)

scale = 1.1

def make_mul(n): 
  def mul(val):
    out = val * n * scale
    return out 
  return mul

mul7 = make_mul(7) 
print(mul7(3))