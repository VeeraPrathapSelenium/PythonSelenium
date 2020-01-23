data="The Temperature is high, due to Thermal power plant"

arr=data.partition("The")
temp=''
for words in arr:

    if not words.isspace() and words.lower()=='the':
        temp=temp+words.replace("The","Yes")

print(temp+" "+arr[2])

