

namestring = input("input list of names here")
list = []

fullname = namestring.split(",")
for x in fullname:
    fullname = x.split(" ")
    list.append(fullname)

list.sort()
print(list)