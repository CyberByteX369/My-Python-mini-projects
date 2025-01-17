'''Write a Python program to create calculator and insert addition
two number, subtraction, multiplication, division, modules & ... '''
def add():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    add=n1+n2
    print('The addition of two numbers is : ',add)
    choose()
def sub():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    sub=n1-n2
    print('The subtraction  of two numbers is : ',add)
    choose()
def mul():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    mul=n1*n2
    print(mul)
    choose()
def divi():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    divi=n1/n2
    print(divi)
    choose()
def modu():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    modu=n1%n2
    print(modu)
    choose()
def flor():
    n1=float(input("Enter first number:-"))
    n2=float(input("Enter second number:-"))
    flor=n1//n2
    print(flor)
    choose()
def tnx():
    print("Thanks for use our calculator you can visit my other mini projects! ")
    

def choose():
    print("choose 1 for Addition")
    print("choose 2 for Subtraction")
    print("choose 3 for Multiplication")
    print("choose 4 for Division")
    print("Choose 5 for Modules")
    print("Choose 6 for Flore Division")
    print("Choose 7 for Exit")
    ch=int(input("Enter choosen number:-"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        divi()
    elif ch==5:
        modu()
    elif ch==6:
        flor()
    elif ch==7:
        tnx()
    else:
        print("Please press (1,2,3,4,5,6,7)")
        choose()    
choose()        