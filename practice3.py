# min-Project Calculator

A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
print("select operation  +   -   *    /   %  ** ")
C =input(" Enter operation : ")


if(C=='+'):
    print("sum is : ",A+B)
elif(C=='-'):
    print("sub is : ",A-B)
elif(C=='*'):
    print("product is : ",A*B)
elif(C=='/'):
    print("division is : ",A/B)
elif(C=='%'):
    print("remender is : ",A%B)
elif(C=='**'):
    print("power is : ",A**B)
else:
    print("invalid input")