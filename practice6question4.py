# WAF to return the aaverage marks if a list of marks is passed as parameter

def avg(marks,size):
    add = sum(marks)
    print("avg of marks : ",add/size)

marks = [3,5,7,2,9,4]
size = len(marks)
avg(marks,size)