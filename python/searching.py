inputList = input("input your list here.make sure it has commas in between each element")
listProper = inputList.split(",")
searchElement = input("what elements do you want to search for")
inList = False
for x in listProper:
    if x == searchElement:
       inList = True

if inList == True: print ("it is in the list at position",listProper.index(searchElement)+1)

else: print("it is not in the list")




