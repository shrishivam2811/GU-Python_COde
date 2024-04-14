employee_directory = {}

def add_employee(id, name, department, contact_info):
   employee_directory[id] = {"name": name,"department": department,"contact_info": contact_info}

def update_employee(id, name=None, department=None, contact_info=None):
        if id in employee_directory:
            if name:
                employee_directory[id]['name'] = name
            if department:
                employee_directory[id]['department'] = department
            if contact_info:
                employee_directory[id]['contact_info'] = contact_info
        else:
            print("Employee not found.")

def get_employee(id):
   if id in employee_directory:
       return employee_directory[id]
   else:
       return "Employee not found."

def get_employee(name):
    if name in employee_directory:
        return employee_directory[name]
    else:
        return "Employee not found."

add_employee(12,'Raj','Tech',9876543210)
add_employee(18,'Mukesh','Tech',1234567890)

update_employee(18,department='Management')

print(get_employee(18))