import json

def menu():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (s) Save students')
    print('\t (l) Load students')
    print('\t (q) Quit')
    option = input('Type one letter (a/v/s/q): ')

    return option

def do_add():
    new_name = "blank"
    while new_name != "":
        new_student = {}
        new_name = input("Enter student name: ")
        if new_name == "":
            break
        new_student['name'] = f'{new_name}'
        add_module(new_student)

def add_module(current_student):
    current_student['courses']=[]
    new_module="blank"
    while new_module != "":
        new_module = input("Enter module name: ")
        if new_module== "":
            break
        new_grade = input("Enter grade: ")
        current_student["courses"].append({"name":new_module,"grade":new_grade})
    students.append(current_student)

def do_view():
    if students == []:
        print('\nNo students loaded!\n')
    for student in students:
        print(f'Name: {student["name"]}')
        print(f"\t{'Subject':<10} Grade")
        for subject in student['courses']:
            print(f'\t{subject["name"]:<10} {subject["grade"]}')
        print('')

def do_save():
    with open('students.json', "wt") as fp:
        json.dump(students,fp)
    print('\nStudents saved!\n')

def do_load():
    print('\nStudents loaded!\n')
    with open('students.json', 'rt') as fp:
        return json.load(fp)


students = []
try:
    with open('students.json', 'rt') as fp:
        students = json.load(fp)
except FileNotFoundError:
    with open('students.json', 'wt') as fp:
        json.dump(students,fp)
option = menu()
while option.lower() != 'q':
    if option == 'a':
        do_add()
    elif option == 'v':
        do_view()
    elif option == 's':
        do_save()
    elif option == 'l':
        students = do_load()
    elif option!='q':
        print('Please choose from a, v, s, l or q.')
    option = menu()
    



