from random import shuffle
import numpy

matrix=numpy.chararray((6,9),)
matrix[:]='a'
days=['Mon','Tue','Wed','Thurs','Fri','Sat']
period=[]
for i in range(0,9):
    period.append(`i+1`)
Lname=[]
name="Name"

def Class():
    for i in range(0,6):
        Lname.append((name+`i+1`))
    Lname.append('LAB')
    shuffle(Lname)
    count=0
    for i in Lname:
        if i=='LAB':
            print i
            count+=3
        elif count!=9:
            print i
            count+=1
        else:   
            print "\n"
            count=0
Class()


