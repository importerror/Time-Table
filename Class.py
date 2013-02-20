from random import shuffle

matri=[]
Lname=[]
name="Name"

def Class():
    for i in range(0,8):
        for j in range(0,8):
            Lname.append(name+`i+1`+`j`)
    for i in range(0,2):
        Lname.append('LAB')
    shuffle(Lname)
    count=0
    for i in Lname:
        if count!=7:
            print i,
            count+=1
        else:   
            print "\n"
            count=0
Class()


