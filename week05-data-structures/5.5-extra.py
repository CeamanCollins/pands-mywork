students = []
new_name = "blank"
while new_name != "":
    new_student = {}
    new_name = input("Enter name: ")
    if new_name == "":
        break
    new_student['name'] = f'{new_name}'
    new_student['courses']=[]
    new_module="blank"
    while new_module != "":
        new_module = input("Enter module name: ")
        if new_module== "":
            break
        new_grade = input("Enter grade: ")
        new_student["courses"].append({"name":new_module,"grade":new_grade})
    students.append(new_student)

print(students)

    