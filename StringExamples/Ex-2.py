data="My Voucher number is 1089"
temp=""
for char in data:

    if char.isdigit():
        temp=temp+char
print(temp)

