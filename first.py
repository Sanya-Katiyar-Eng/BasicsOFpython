print(".................Python basics......................")
print("swap to num without using third variable")
a=9
b=7
print("befor swap : a=",a,"b =",b)
a=a+b
b=a-b
a=a-b
print("after swap : a=",a,"b =",b)
print("find largest num ")
a=9
b=7
c=1
if(a>b and a>c):
    print("largest :",a)
elif(b>a and b>c):
    print("largest :",b)
else:
    print("largest",c)
print(" find num is even or odd : ")
a=int(input("enter the num for finding even or odd:"))
if(a%2==0):
    print(a," is even")
else:
    print(a," odd")
a=int(input("enter the first num for perform operation(+,-,*,/,%) :"))
b=int(input("enter the second num for perform operation:"))
print("add :",a+b)
print("substraction :",a-b)
print("multiply ",a*b)
if(a>b):
    print("divided ",a/b)
else:
    print("divided ",b/a)
print("module :",a%b)
print("module :",b%a)
print("1 to 10 num using for loop")
for x in range(1,10):
    print(x)
x=1
print("1 to 10 num using while loop")
while(x<10):
    print(x)
    x+=1
print("multiplection table")
n=int(input("enter the num for multiplection table "))
for x in range(1,n):
    print("table for :",x)
    for i in range (1,11):
        print(i,"*",x,"=",i*x)
i=1
j=1
while(i<n):
    print("table for ",i)
    i=i+1
    while(j<11):
        print(i,"*",j,"=",i*j)
        j=j+1
print("sum of n num ")
count=0
for x in range(1,10):
    count+=x
print("sum of 10 num ",count)
x=10
while(x>1):
    print(x)
    x=x-1
num=int(input("enter the num for reverce num:"))
a=0
while(num!=0):
    a=a*10
    temp=num%10
    a+=temp
    num=num//10
print(a)

print("febonachi series ")
num=int(input("enter the num "))
a,b,c=0,1,0
for x in range(1,num):
    print(c)
    a=b
    b=c
    c=a+b
str=input("enter string ")
count=0
print(str)
print("length ",len(str))
print("lowercase ",str.lower())
print("uppercase ",str.upper())
rev=str[::-1]
print("reverse string:",rev)
if(rev==str):
    print("string is palindrom")
else:
    print("not palindrom")
print("list basics ")
l=[9,6,4,2,7,1]
max=l[0]
min=l[0]
print(type(l))
for x in range(0,len(l)):
    if(max<=l[x]):
        max=l[x] 
print("max ",max)
for x in range(0,len(l)):
    if(min>=l[x]):
        min=l[x]
print("min :",min)
l.append(9)
l.append(4)
l.append(4)
print(l)
l.pop()
print(l)
for x in range(1,len(l)):
    key=l[x]
    j=x-1
    while(j>=0 and l[j]>key):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print("sorted list with insertion sort",l)
count=0
print(l.sort())
print(l)
for x in range(0,len(l)):
    count+=l[x]
print("sum of list  is :",count)
l1=[8,5,0,2]
l2=[9,0,2]
print(l1+l2)
l=[4,9,0,5,2,9,0,1]
le=[]
for i in range(len(l)):
    if(l[i] not in le):
        le.append(l[i])
print(le)
l1=[9,0,6,5,9]
l2=[9,6,3,1,9,9,9,1]
l=[]
lc=[]
for i in range(len(l1)):
        if (l1[i] in l2):
            l.append(l1[i])
for x in range(len(l)):
      if l[x] not in lc:
            lc.append(l[x])
print(lc)
l=[0,7,5,3,9,8,1,0]
leven=[]
lodd=[]
for x in range(len(l)):
    if(l[x]%2==0):
        leven.append(l[x])
    else:
        lodd.append(l[x])
print("even list :",leven)
print("odd list :",lodd)
print("........tuples basics............")
t=(8,7,9,0,0,-8)
print(t,type(t))
l=list(t)
print(l,type(l))
count=0
for i in range(len(t)):
    if t[i] in t:
        count=count+1
        print(t[i],count)
    count=0
max=t[0]
min=t[0]
for i in range(len(t)):
    if max<t[i]:
        max=t[i]

print("max in tuples:",max)
for i in range(len(t)):
    if min>t[i]:
        min=t[i]
print("min in tuple :",min)
num=input("enter the value for finding value in tuple or ")
if num in t:
    print("num find")
else:
    print("not found")
print("Unpack tuple")
t=(1,2,3)
a,b,c=t
print(a,b,c)
x,*y,z=t
print(x,y,z)
print(type(x),type(y),type(z))
print("..........set basics..............")
s1={7,9,0}
s2={0,5,3}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
t=(8,7,5,3,1,9,0,7,5,2)
s=set(t)
print(t)
print(s)
l1=[0,7,5,3]
l2=[0,4,2,5]
s1,s2=set(l1),set(l2)
print(s1.difference(s2))
print("............dict basics..............")
dict={"aman":90,"riya":78,"komal":45,"tata":67}
print(dict)
dict["kajal"]=90
dict.pop("aman")
print(dict)
dict.update({"ram":67,"seeta":90})
print(dict)
print(dict.keys())
print(dict.values())
max=0
for i,j in dict.items():
    if max<j:
        max=j
for i,j in dict.items():
    if j==max:
        print(j,i)

sentence="seeta is a good girl and she is brave"
dict={}
s=sentence.split()
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
dict={"ram":90,"gyh":67,"uhi":67}
print(sorted(dict.items()))
d={"jih":8,"hvd":90,"dsc":8}
l=list(d.values())
print(l)
print("..........functions basics............")
def fun(a,b):
    return a+b
c=fun(5,7)
print(c)
def prime(num):
    for n in range(2,num):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n,"\t ")
prime(10)
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
a=fact(4)
print(a)
sequre=lambda x:x*x
print(sequre(5))