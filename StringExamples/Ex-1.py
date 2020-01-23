data="My Transaction number is (1089)"

#Do not use any looping condition to extract the number

pos1=data.find("(")+1

pos2=data.find(")")

print(data[pos1:pos2])

# String slicing

'''

string[start position(index):length]



'''





