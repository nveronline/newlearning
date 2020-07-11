inputList = input("input your list here.make sure it has commas in between each element")
listProper = inputList.split(",")
print("if you want to order from least to greatest press 1")
print("if you want to order from greatest to least press 2")
leastOrGreatest = input("press 1 or 2")

if leastOrGreatest == '1':
    listProper.sort(reverse=False)
    print("this is the list",listProper)
elif leastOrGreatest == '2':
    listProper.sort(reverse=True)
    print("this is the list", listProper)
else:
    print("improper value")
