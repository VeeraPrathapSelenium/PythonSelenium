class Employee:

    def __init__(self,name,sal):
        self.__name=name # Private
        self.__sal=sal #Private

class HR(Employee):

    def task(self):

        print("HR department will mangae the projects")


obj=HR("KRISH",45000)
print(obj.__name)
print(obj.__sal)




