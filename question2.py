# print all odd number 1 to 20 
for i in range(1,20,2):
    print(i)

# print the table of 57
for i in range(1,11):
    print("57 X ",i ,"= ", 57*i )

# Print all multiples of 3 from 1 to 50 but skip 15
for i in range(1,51):
    if(i==15):
        continue
    if(i%3==0):
        print(i)

# take two integers a and b as input.
# find and print the first number between 1 and 1000 that is divisible by both number 

A = int(input("enter first number : "))
B = int(input("enter second number : "))

for i in range(1,1001):
    if(i%A==0 and i%B==0):
        print(i)
        break