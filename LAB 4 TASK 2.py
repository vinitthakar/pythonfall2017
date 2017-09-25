import reduce
def even_sum(lists):
   y=reduce(add,lists)
return y


def add(a,b):
   z=a+b
return z 




s=[]
for element in range(100,501,2):
   s.append(element)
   print(s)
   x=even_sum(s) 
   print(x)


