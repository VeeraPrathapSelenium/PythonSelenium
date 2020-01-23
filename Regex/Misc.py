import re

data="My native place is HYDERaBAD and stay at KPHB and my salaray is 55000"

patrn="[^0-9]"

result=re.sub(patrn,"",data)

print(result.strip())

