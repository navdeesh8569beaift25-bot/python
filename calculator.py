a=input("enter symbol")
b=int(input("enter number"))
c=int(input("enter number"))
if a=='+':
    print("addition",b+c)
elif a=='-':
    print("subtraction",b-c)
elif a=='/':
    print("division",b/c)
elif a=='%':
    print("remainder",b%c)
else:
    print("invalid")