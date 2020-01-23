def add(*args):
    argLength=len(args)
    temp=0
    for x in args:
        temp=temp+int(x)
    print("Sum of "+str(argLength)+" numbers is "+str(temp))


add(1,2,8,8)
