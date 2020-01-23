class Employee:

    YearOfExperince=0

    def __init__(self,name,age,salary):
        print("i am paramterized constructor")
        self.name=name
        self.age=age
        self.salary=salary


    def add_Employee(self):
        print("Employee {0} is created sucessfully ".format(self.name))

    def del_Employee(self):
        print("Employee {0} is deleted sucessfully ".format(self.name))








