import random
x = [3,1,9,3,123]
def is_sorter (x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return False
def swap(x,i,y):
            x[i], x[y] = x[y], x[i]
def r (P):
  return random.randint(0,P-1)



while True:
   if is_sorter(x) == True:
       print(x,"ок")
       break
   else:
       swap(x,r(len(x)),r(len(x)))





