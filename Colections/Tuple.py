data=(1,5,4,3,3)

#Length

print(len(data))

#Acces the item from a tuple

print(data[0])

#iterate over loop

for x in data:
    print(x)

print("****************************************")

# print using a range loop

for x in range(0,len(data)):
    print(data[x])
print("**********************")
# check with negavtive index:

print(data[-1])
print("******************************")

print(data[0:2])

print("*************************")

print(156 in data)

print("************************")

mytuple=("prathap",)
print(type(mytuple))
print("***********************")

print(data+mytuple)

print("***********************")

print(data.count(3))
print(data.index(1))
