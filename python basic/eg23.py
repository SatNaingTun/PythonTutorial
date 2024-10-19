import random


numbers=[1,2,3]

for x in numbers:
    new_number=x+1
    print(new_number)

names1=["Alex","Beth","Caroline","Dave","Elenaor"]

names=['Alice','Bob','Cara','David','Erika','Fred']
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

passed_students={key:value for (key,value) in student_scores.items() if value>=60}
print(passed_students)



