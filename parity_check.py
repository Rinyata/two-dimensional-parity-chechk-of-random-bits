import random

ary = []
arytemp = []
sum = 0

for i in range (0,5):
    arytemp=[]
    for j in range(0,5):
        arytemp.append(random.randint(0,1)) #generating random 0s and 1s for a temporary array
    ary.append(arytemp) #transferring temporary array to main array by using append method

arytemp = [] #gonna reset temporary array

for i in range(0,5):
    sum = 0
    for j in range(0,5):
        sum += ary[i][j] #we add the numbers in the rows in order and add them to the sum
    sum = sum%2 #looking if the sum is even or odd
    ary[i].append(sum) #appending  the checksum number to the end of the array

for i in range(0,5):
    sum=0
    for j in range(0,5):
        sum += ary[j][i] #doing the same thing but for the columns
    sum = sum%2
    arytemp.append(sum) #created a new temporary array and we put sum numbers to it
ary.append(arytemp) #appending temp array to the main one

for i in range(0,6):
    print(ary[i]) #print out final result
