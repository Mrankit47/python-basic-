# WAF to print if a number is prime or not

def prime(num):
    prime = 0;
    for i in range(2,num):
        if num%i==0:
            prime+=1

    if(prime==0):
        print(" prime")
    else:
        print("not prme")

num = int(input("Enter any number : "))
prime(num)
