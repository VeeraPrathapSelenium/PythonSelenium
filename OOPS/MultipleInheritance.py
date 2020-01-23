class Parent1:

    def add(self):
        print("Adding two numbers from Parent1")

class Parent2:

    def add(self):
        print("Adding two numbers from Parent2")

class child(Parent2,Parent1):

    pass


obj=child()
obj.add()

