class A:

    x=1
class B(A):
    y=20

class C(A):
   z='prathap'

class D(A):
    pass




obj=C()
print(obj.x)
print(obj.z)
