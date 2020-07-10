list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = float(input('Enter number '))
    list.append(numbers)

max=list[0]
for x in list :
    if x>max :
        max=x
print (max)
