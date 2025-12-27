import random
class BankAccount:
    name=input("Enter your name :")
    address=input("Enter your address :")
    account=random.randint(100000000,10000000000)
    count=int(input(".........deposite some money for creating your account............. \n minimum money which you can deposite is 1000 :\n Now!!Enter the money :"))
    if(count<1000):
        print("plase ! Enter valid amount you deposit only",count,"\nthat was not enough plzz min deposite 1000")
        print("now you cant register ")
    else:
        def __init__(self):
            print("..............Welcome.................")
            print(".............UMETU BANK.................")
            name=self.name
            address=self.address
            print("your account num :",self.account)
            self.bankstatus()
        def deposite_money(self):
            money=int(input("Enter the money : "))
            self.count+=money
            a=int(input("Enter \n1 if you want to cheak any thing \notherwise enter 2 for exit"))
            if a==1:
               self.bankstatus()
            else:
                print("...........Thanks..............")
                print(".........plzzzz give me your experience..........")
                ex=input("your expirence : ")
        def withdrow_money(self):
            money=int(input("enter withdrow money : "))
            if(money<self.count):
                self.count-=money
                print("Now ! \nyour current ballance ",self.count)
            else:
                print("you have not enough money")
                print("your current ballance is ::",self.count)
            a=int(input("Enter \n1 if you want to cheak any thing \notherwise enter 2 for exit"))
            if a==1:
               self.bankstatus()
            else:
                print("...........Thanks..............")
                print(".........plzzzz give me your experience..........")
                ex=input("your expirence : ")
        def current_status(self):
            print("..............Your current status............ ")
            print("your name :",self.name)
            print("account number :",self.account)
            print("bank ballance :",self.count)
            print("your address :",self.address)
            a=int(input("Enter \n1 if you want to cheak any thing \notherwise enter 2 for exit"))
            if a==1:
               self.bankstatus()
            else:
                print("...........Thanks..............")
                print(".........plzzzz give me your experience..........")
                ex=input("your expirence : ")
        def bankstatus(self):
            num=int(input("What you want \n 1:cheak status \n2:Deposite money\n3:Withdrow money\nEnter the num :"))
            if num==1:
                self.current_status()
            elif num==2:
                self.deposite_money()
            elif num==3:
                self.withdrow_money()
            else:
                print("you enter wrong num       Now you have only one chance ")
                a=int(input("Enter \n1 if you want to cheak any thing \notherwise enter 2 for exit"))
            if a==1:
               self.bankstatus()
            else:
                print("...........Thanks..............")
                print(".........plzzzz give me your experience..........")
                ex=input("your expirence : ")
obj=BankAccount()
    