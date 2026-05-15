student = ["Mark","Chris","Franke","Paraj"]

# student2 = student
student2 = student.copy()

print(student2)

# for i in student:
#     print(i)

student.append("Andrea") 
student.sort()

print(student[-1]) # last element in the list

for i in range(len(student)):
    print(student[i])




