# given a list of roll number [101,105,102,101,108,105,110] print all unique roll numbs in the list

roll_num = [101,105,102,101,108,105,110]

unique=set(roll_num)

lis = list(unique)
print(lis)

# given Employee record in the form of a list of tuples where each tuple contains:
# (Employee Id, Employee Name, Salary)
# Example = [(101,"Ankit",55000),(102,"joan",45000),(103,"rahul",34000)]
# ask user to enter Employee id & search it inside records

Example = [(101,"Ankit",55000),(102,"joan",45000),(103,"rahul",34000)]

emp_id = int(input("enter emp_id : "))

found = False

for exp in Example:
    if(emp_id==exp[0]):
        print("Employee All details")
        print("employee id : ",exp[0])
        print("employee name : ",exp[1])
        print("employee salary : ",exp[2])
        found = True
        break
if found == False:
    print("emp not found ")
