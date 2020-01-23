class School:

    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std

    def addStudent(self):
        print("Student {0} is added to the DB".format(self.name))

    def delStudent(self):
        print("Student {0} is deleted from the DB".format(self.name))

    def searchStudent(self,id):
        print("Student {0} is serched by the id ".format(self.name))


class DPS(School):

    #def __init__(self,name,age,std):
     #   self.name=name;
      #  self.age=age
       # self.std=std


    def __init__(self):
        super().__init__('Raj',25,10)


    def add_Student_to_music(self):
        print("Student is added to the music school")

    def add_student_to_library(self):
        print("Student is added to library")




obj=DPS()
obj.addStudent()
obj.add_Student_to_music()
obj.add_student_to_library()
