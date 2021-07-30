# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:36:28 2021

@author: Dell
"""

Chapter 3 #tuples

#method1: using ()

t1=(2,4,6,8,10)
type(t1)

t2=(12,4.5,"ddd",True)
print(t2)

type(t2)

t2[3]

len(t2)

#------------------


t3=5,10,15,20
type(t3)
#create a tuple of a single value------------

t4=(10) #this ia a variable
t5=10#this is a variable

t6=(10,) #put a comma after the number create a tuple
type(t6)

t7=10,
type(t7)


#method2; using tuple function

print(range(1,6))

x=tuple(range(1,10))
print(x)
type(x)
print(x)
sum(x)
max(x)
min(x)
len(x)

#----------------
y1=("a","b")
len(y1)

y1+("c","d")
y1

y1=y1+("c","d")
y1

b="e",
y1=y1+b
y1

y1+="f"  #gives an error,as its not a tuple,put a comma to repair it

y1 +=("f",) #y1=y1+("f",)
len(y1)
y1[2]

#indexing in yuple----
y1=('a','b','c','d','f','f')
len(y1)
y1[2]
y1[0:2] #end-1

y1.index("c")
y1.index("f")
y1.count("f")

ob1=y1[2]
type(ob1)

ob2=y1[0:2]
type(ob2)

#-----------------
y1[1]="t" #error:tuple is immutable

t3=(12,"age",(True,100)) #nested tuple
len(t3)
t3[2]


t3[2][1] #to access the inner value
t3[2][0]

#tuple ...not in and in---------------
12.5 in t3
12.5 not in t3

100 in t3
(True,100) in t3

100 in t3[2]

t3.index((True,100))
#----------------------

t4=(1,2)
t4*5
t5=t4*5
t5

#-------------
#multi.assign.
#95,90,85

m1=95;m2=90;m3=85

(m1,m2,m3)= (75,60,55)
type(m1)
#---------------

#unpacking

data=(75,60,55)
(x,y,z)=data
x
type(x)

#-------------
(a,b,c)=range(1,4) #mult.assig,
a
b
c

#----------
#swap

x=10
y=20

temp=x  #temp:10
x=y     #x:20
x
y

#-------------
#sol2
x=10
y=20

#swap using tuple
(x,y)=(y,x)
x
y

#-----------
num2=tuple(range(10,20))
num2

num2[2:6]
num2[2:]
num2[:4]

#----------------------------
#List 
#method1:[]

x=[12,5,7,"dd",True]

type(x)
x[0]=20
len(x)
x

#method2; list()

z=list(range(25,30))
z
type(z)

[2,3,4]*2

z*3

z[0]*2 #25*2=50

z[0]=z[0]*2
z
type(z)
type(z[0])
#--------------------------

list(range(1,10)) #forward step=1

list(range(1,10,2)) #step=2

list(range(0,11,2))

list(range(5,51,5))

list(range(10,1, -3)) #step backwards=-3

list(range(100,0, -10)) 

#-------------------------------
z=[12,5,7,["dd",'gg'],True] #nested list
len(z)
z[3][1]  #to get 'gg'

z=[12,5,7,["dd",'gg'],True]
z
z[3][1]="hh" #error
z[3]=["ss",'hh']
z
#-------------------

a=['aa','bb']
b=['cc']
a+b
a+"ff" #error

a
#--------append(adding a value at the end of a list)------

a
a.append("ff") #adding a single value
a


fruits=['apple','banana','cherry']
fruits.append("orange")
fruits
 
#looping--------------------------------------------------
for x in fruits:     
    print(x)

for f in fruits:
    print(f)
    
for n in fruits:
    print(n, end=" ")
    
len(fruits)    #the num of values in the list

len(fruits[2])  #length of cherry

for f in fruits:
    print(len(f)
          
#-----------------------------

t=(1,2,3,4,5,)
res=[]

for x in t:
    z=x*10
    res.append(z)
    
print(res)

#------------------------------------
 #looping optimization---
 res2=[]
 for x in t:
    res.append(1*10)
 
print(res2)

#-----------------Sum in loop

salary=[20,30,50,70]

sum(salary)       #sum method

total=0
for s in salary:
    total=total+s

total

for s in [0,1,2,3]:
    print(salary[s])
    
#--------------------LOOPING ____-
    
  
fruits=['apple','banana','cherry']
if "apple" in fruits:
    print("found")
#---------------------
12%2
13%2

t=tuple(range(0,11))
t
for t in range(0,11,3):
    print('t',end=" ")
 

#---------------------------------
#while;

a=["tt","rr","yy","uu"]

for i in a:
    print(i)
    

j=0

while j<len(a):    #j <4: j=0
    print(a[j])
    j=j+1
    
#--------Append and Extend and Insert and Remove and Pop------

a=["apple","banana","cherry"]
b=["Ford","BMW","Volvo"]

a.append(b)
a

a=["apple","banana","cherry"]
a.extend(b)
a


aList=[123,'xyz','zara','abc']
aList.append(1000)
aList

aList.insert(3,2020)   #insert(index,value)
aList

aList.remove('xyz')      #delete by value
aList

aList.pop(0)     #delete by value
aList

year=aList.pop(1) #delete by value and keep the removed value
year

#---Sorting---------------
v=[12,5,33,6,77,89]
v
len(v)

sorted(v)
v

v1=sorted(v)
v1

v.sort()

#-------------
v=[12,5,33,6,77,89]

sorted(v,reverse=True)
#-------------
names=["foysal","anna","sherin","chika","zainb"]
sorted(names)
sorted(names,reverse=True)

#uppercase goes first before lowercase
#A,B,C---------------Z,a,b,c.........z
"John"=="john"
"John"<"john"
"Zara"<"anna"

#----------------
max([12,4,77])

max(names)

min(names)

max(names,key=len) #max num of character

#-------------------
#list comprehension syntax

number=list(range(1,11))
number
for x in number:
    print(x/2)

for i in number:
    if i%2 == 0:
        print(i)
        
number
even_number=[i for i in number if i%2 ==0]
number
even_number


#----------------------------
#Example A manager asked you to get 30% off in pricing for an item

price=[12,13,16,110,60,22]

for p in price:
    print(p*0.7)
    
    
#return_value loop cond-------------

names =["apple","banana","cherry","orange"]
length=[len()]


names=["apple","banana","cherry"."orange"]
max(names)

[len(j) for j in names]

max([len(j) for j in names])

max(names,key=len)

[n for n in names if len(n)== len(max(names,key=len))]
