'''
Data="AB65DFV41HNG26"

65+41+26=?
verify this number is a prime or not
'''
import re

Data="AB65DFV49781HNG26"

x=re.sub("[A-Za-z]","@",Data)

arr=re.split("\@",x)
temp=0
for i in arr:

    if(len(i)>0):
        temp=temp+int(i)

print(temp)

