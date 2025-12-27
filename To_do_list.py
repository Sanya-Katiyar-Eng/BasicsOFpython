import datetime
name=input("Enter your Full name : ")
task=input("Enter your Goal: ")
print("Hello!",name,"\nWelcome!\nI hope that to do list help you \nToday's Date & time :",datetime.date.today(),"\n\nplzzzz make yor list as you want to follow step by step")
num_of_line=int(input("inter the num of line :"))
list=[]
dict={}
for i in range(num_of_line):
    print("write your ",i)
    n=input("work : ")
    dict[i]=n
print("If you want to see your todo list Enter 1")
n=int(input("enter :"))
if(n==1):
    for i,j in dict.items():
        print(i,":",j)
else:
    print("Your to do list is created\nThanks for using this code\nplzz fallow it regularlly Sothat you can improve your self  \n")

