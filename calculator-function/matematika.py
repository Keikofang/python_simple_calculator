def add(x,y):
  return x + y
def subtract(x, y):
  return x-y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y

def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n*recur_factorial(n-1)

def recur_fibo(n) :
  if n <= 1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

def hcf(x,y):
  if x > y:
    smaller = y
  else:
    smaller = x
  for i in range(1,smaller +1):
    if((x %i == 0) and (y % i == 0)):
      hcf = i
  return hcf