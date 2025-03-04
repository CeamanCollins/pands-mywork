def menu():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (q) Quit')
    option = input('Type one letter (a/v/q): ')

    return option

def do_add():
    new_name = "blank"
    while new_name != "":
        new_student = {}
        new_name = input("Enter name: ")
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
    for student in students:
        print(f'Name: {student["name"]}')
        print(f"\t{'Subject':<10} Grade")
        for subject in student['courses']:
            print(f'\t{subject["name"]:<10} {subject["grade"]}')
        print('')

students = []
option = menu()
while option.lower() != 'q':
    if option == 'a':
        do_add()
    elif option == 'v':
        do_view()
    elif option!='q':
        print('Please choose from a, v or q.')
    option = menu()
    



