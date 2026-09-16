# complex data type of python

# List is mutable

marks = [55,33,77,88,99,22]

print(sum(marks))

print(len(marks),marks,type(marks))

# indexing
print(marks[-1])

# sliceing

print(marks[0:4])

# loop in list

for score in marks:
    print(score)

# add value last in list
marks.append(67)
print(marks)

# add paritcular index 
marks.insert(0,89)
print(marks)

# Tuple is imutable
mark = (55,67,34,78)

print(type(mark))

print(mark.count(78))
print(mark.index(78))

# set datatype unique items collection

mar = {98,92,34,54,44,34,54}

print(len(mar))

# dictionary key value mutable data type

student1={
    "Math":99,
    "scince":76
}
student1['english']=90
student1['hindi']=99

print(student1)
for key in student1:
    print(key,student1[key])


lis = []
tup = ()
sett = set()
dic = {}

print(type(lis))
print(type(tup))
print(type(sett))
print(type(dic))