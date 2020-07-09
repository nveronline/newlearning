m=input ("enter number:")
y=input  ("enter number:")
z=input  ("enter number:")
Operation=input ("enter operation which you want to do as a symbol:")

if Operation == '+':
    sum = float(m) + float(y) + float(z)
    print("The sum of {0},{1}, and {2}  is {3}" .format(m, y, z, sum))

elif Operation == '-':
    sum = float(m) - float(y) - float(z)
    print("The subtraction of {0},{1}, and {2}  is {3}" .format(m, y, z, sum))

elif Operation == '*':
    sum = float(m) * float(y) * float(z)
    print("The multiplication of {0},{1}, and {2}  is {3}" .format(m, y, z, sum))

elif Operation == '/':
    sum = float(m) / float(y) / float(z)
    print("The division of {0},{1}, and {2}  is {3}" .format(m, y, z, sum))

else:
    print ("i cannot do that")
