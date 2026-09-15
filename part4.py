n = int(input("enter a number : "))
print(range(1,5))


# while loop
count=1
while(count<=5):
    print("Ankit")
    count+=1

# for loop
for i in range(1,6):
    print(i)

# print eve number

for i in range(1,11,):
    if(i%2==0):
        print(i)


for i in range(2,11,2):
        print(i)


# break and continue

for i in range(1,51):
     if(i==21):
          continue
     if(i%3==0):
          print(i)