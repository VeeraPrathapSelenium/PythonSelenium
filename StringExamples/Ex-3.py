data="The Transaction Data : 1089 the Voucher Number :7852 the Processing id :5689 "

#The Transaction Data : 1089
#The Transaction Data : 1089

temp=""
for i in range(0,len(data)):

    if data[i].isdigit() and data[i+1].isspace():
        temp=temp+data[i]+"@"
    else:
        temp=temp+data[i]

arr=temp.split("@")
print(arr)
for sentence in arr:
    print(sentence.strip().title())


