print(".........object oriented programming language concept...........")
class oops:
    print("my oops class is created")
    _x=int(input("enter the val "))
    def __init__(self):
        print("that is constructor")
    def sequre(self):
        print(self._x*self._x)
class G_parent:
    def showG(self):
        print("grant parent class")
class parent(G_parent):
    def showP(self):
        print("parent class")
class child(parent):
    def showC():
        print("child class")

class A:
    def __init__(self):
        print("parent constructor ")
class B(A):
    def __init__(self):
        super().__init__()
        print("child constructor")
class overloding:
    def add(self,a,b=0,c=0,d=0,e=0,f=0):
        print("addition is:",a+b+c+d+e+f)
class overriding1:
    def sum(self,a,b=0):
        print("parent class addition",a+b)
class overriding2(overriding1):
    def sum(self,a,b=0):
        print("child class addition:",a+b)

o=oops()
o.sequre()
print(o._x)
print("..............inheritence with method..........")
O1=child()
O1.showP()
print(".............inheritance with counstructor...............")
O2=B()
O3=overloding
O3.add(6,9,)
O4=overriding2()
O4.sum(7,8)