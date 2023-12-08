import numpy as np
import math
from itertools import combinations

def factorial(n:int) -> int:
  return math.factorial(n)
  # return np.prod([i for i in range(1,n+1)])
 

def combination(lst,n):
  comb = combinations(lst,n)
 
# Print the obtained combinations
  print("Combinations")
  for i in list(comb):
    print (i)
  

def exponential(n):
  return math.exp(n)
  

def compliment(n):
  return ~n
  

