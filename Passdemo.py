x = 5

def fun():
   x=100
   globals()['x']=200
   print(x)
   #print(id(x))

fun()
print(x)
#print(id(x))