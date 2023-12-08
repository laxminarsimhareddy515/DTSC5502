
def hello_dtsc5502():
  print("Hello DTSC5502! This is great")

def greetings ( name : str)-> str:
  print("Hello "+ name + " from the greetings function")

def calculate_mean(lst : list) -> float:
  return sum(lst)/len(lst)

def calculate_median(lst : list) -> float:
  lst.sort()
  m=len(lst)//2
  if len(lst)%2==0 :
    return (lst[m-1]+lst[m])/2
  else :
    return (lst[m])

def calculate_mode(lst : list) -> float:
  count={}
  for item in lst:
    if item in count:
      count[item]+=1
    else:
      count[item]=1
  return [key for key in count if count[key] == max(count.values())]
