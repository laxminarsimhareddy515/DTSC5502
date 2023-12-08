"""import dtsc5502 as dt

def main():
  dt.hello_dtsc5502()
  dt.greetings(' Laxmi Narsimha Reddy')
  


lst = [1,3,7,2,5,7,9]

if __name__== '__main__':
  main()
  #print(dt.greetings('Laxmi Narsimha'))
  print(dt.calculate_mean(lst))
  print(dt.calculate_median(lst))
  print(dt.calculate_mode(lst))
"""


from dtsc5502 import probabilities
from dtsc5502.version import __version__
import dtsc5502.statistics as stats
import dtsc5502.probabilities.functions as probs


print(__version__)
lst = [1,2,1,3,2,2]
print()
print("Mean : ", stats.descriptive.mean(lst))
print("Median : ", stats.descriptive.median(lst))
print("Mode : ", stats.descriptive.mode(lst))

print("Factorial : ", probs.factorial(5))
print("Exponential : ", probs.exponential(4))
print("compliment : ", probs.compliment(4))

print("-------------------------------------")
probs.combination(lst,3)