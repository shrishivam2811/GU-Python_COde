student_records = {}

def add_student(name, age, subjects):
    student_records[name] = {'age': age, 'subjects': subjects}

def update_student(name, age=None, subjects=None):
    if name in student_records:
        if age:
            student_records[name]['age'] = age
        if subjects:
            student_records[name]['subjects'] = subjects
    else:
        print(f"Student {name} does not exist.")

def get_student(name):
    if name in student_records:
        return student_records[name]
    else:
        return "Student not found"

# Add Student
add_student('Shiv',17,'Math')
add_student('Raj',18,'History')
print(f'Student Record:\n {student_records}')

# Update Student
update_student('Shiv',age=16)
print(f'Student Record after update:\n {student_records}')

# Retrieve record 
print(f'Raj : {get_student('Raj')}')