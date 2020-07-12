class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print(self.name, self.age)

# Here is start of my program
numOfPersons=int(input("input the amount of people here:"))

list=[]

for x in range(numOfPersons):
    fname=input("first name please:")
    #lname=input("last name please:")
    age=int(input("age please:"))
    personVariable = Person(fname,age)
    personVariable.printname()
    list.append(personVariable)

#2print(list)

#list.append( Person('Akash', 2))

for obj in list:
    obj.printname()
    #print( obj.name, obj.age, sep =' ' )



