marks1 =[94.3, 78.9, 68.4,99.8,56.8]
print(marks1)
print(type(marks1))
print(len(marks1))
print(marks1[0])
print (marks1[4])
student = ["ram",90.5,15,"Delhi"]
print(student)
print(student[0])
student[0] = "arjun"
print(student)

#List Slicing
marks2 = [85,94,76,63,48]
print(marks2[1:4])
print(marks2[:5])
print(marks2[0:])

#List Methods
list1 = [2,1,3]
list1.append(4)
print(list1)#[2,1,3,4]

list2 = [2,1,5,4,3]
list2.sort()
print (list2)#[1,2,3,4,5]

print(list2.sort(reverse=True))
print(list2)#[5,4,3,2,1]

list = [2,1,3]
list.insert(1,5)
print(list)#[2,5,1,3]

list = [2,1,3,1]
list.pop(2)
print(list)#[2,1,1]




