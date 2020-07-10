numlist=input ("input list:")
list=numlist.split(",")

    #print (list)
    #print (len(list))
    #print (list[len(list)-1])
i=len(list)-1
while i >=0 :
    print (list[int(i)])
    i -= 1
print ("Loop ended")
