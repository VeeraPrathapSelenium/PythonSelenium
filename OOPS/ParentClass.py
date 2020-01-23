class Parent:

    name='prathap'
    age=50
    place='hyd'

    def create_SomeMethod(self):
        print("xyz")


class Child(Parent):

    def __init__(self):
        print(self.name)


obj=Child()
print(obj.age)
print(obj.place)
