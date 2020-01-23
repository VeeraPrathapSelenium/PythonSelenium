class Employee:

    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal


    def getId(self):

        return self.__id

    def getName(self):

        return self.__name

    def getSalary(self):
        return self.__sal


list_obj=[]
for i in range(1,21):

    obj=Employee(i,'Krish'+str(i),52000*i)
    list_obj.append(obj)

for i in range(len(list_obj)):

    print(list_obj[i].getName())
    print(list_obj[i].getId())
    print(list_obj[i].getSalary())



