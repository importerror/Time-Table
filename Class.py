from random import shuffle
import numpy

matrix=numpy.chararray((7,9),itemsize=10)
matrix[:]='None'
days=['Mon','Tue','Wed','Thurs','Fri','Sat']
period=[]
for i in range(0,9):
    period.append(`i+1`)
Lname=[]
name="Name"

def Class():
    j=1
    for i in days:
        matrix[[j],[0]]=numpy.array([i])
        j+=1
    j=0
    for i in period:
        matrix[[0],[j]]=numpy.array([i])
        j+=1
    print matrix
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
<<<<<<< HEAD
=======

>>>>>>> 2aee3b625fddd8d8af0de11df75d330016b65d3b
