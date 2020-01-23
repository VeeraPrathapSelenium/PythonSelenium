class Student:

    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age


# lets create an object to this class
obj=Student("Prathap",404,29)

print(obj.__dict__)

print(obj.__doc__)

print(obj.__module__)

print(obj.__name__)
