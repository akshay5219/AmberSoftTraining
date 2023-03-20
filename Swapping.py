a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("A = {} and B = {}".format(a, b))
a = a + b
b = a - b
a = a - b
print("Now, A = {} and B = {}".format(a, b))