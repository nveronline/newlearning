class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print(self.name, self.age)

namestring = input("input list in the following format {name.age [,]}...")
list = []

fullname = namestring.split(",")
for nameagepair in fullname:
    nameagelist = nameagepair.split(".")
    p1 = Person(nameagelist[0],int(nameagelist[1]))
    list.append(p1)

for obj in list:
    obj.printname()



