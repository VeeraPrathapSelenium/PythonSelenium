import re

inputString="My email address is firstname.lastname@tcs.com";

pattern="[a-z0-9]*\.[a-z0-9]*\@tcs\.com"
'''
x=re.search(pattern,inputString)

print(x.span())
print(x.start())
print(x.end())

print(inputString[x.start():x.end()])
'''

x=re.findall(pattern,inputString)

for ptn in x:
    print(ptn)

'''
x=re.split("\s",inputString)

print(x)
'''