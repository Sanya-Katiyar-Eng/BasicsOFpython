print(".........object oriented programming language concept...........")
class oops:
    print("my oops class is created")
    _x=int(input("enter the val "))
    def _init_(self):
        print("that is constructor")
    def sequre(self):
        print(self._x*self._x)
print("..............inheritence with method..........")
class G_parent:
    def showG(self):
        print("grant parent class")
class parent(G_parent):
    def showP(self):
        print("parent class")
class child(parent):
    def showC():
        print("child class")
print(".............inheritance with counstructor...............")
class A:
    def _init_(self):
        print("parent constructor ")
class B(A):
    def _init_(self):