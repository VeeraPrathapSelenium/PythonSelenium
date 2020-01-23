class A:

    x=20
    z=30
    def add(self,a,b):
        print("Sum of two numbers is "+str(a+b))

class B(A):

    def add(self,a,b):

        print(self.x)
        print(self.z)

        print(super().x)
        print(super().z)

        print("I am adding two numbers "+str(a+b))

obj=B()
obj.add(10,20)