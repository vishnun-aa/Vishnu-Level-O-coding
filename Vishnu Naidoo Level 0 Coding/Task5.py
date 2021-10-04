a = float(input("Enter the first side"))
b = float(input("Enter the second side"))
c = float(input("Enter the third side"))

Perm = (a+b+c)
x = Perm/2
area = (x*(x-a)*(x-b)*(x-c))**0.5


print("area equals :",area)
