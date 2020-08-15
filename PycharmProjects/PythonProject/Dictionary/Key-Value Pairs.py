student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student.get('phone', 'Not Found'))
student.update({'name': 'Jane', 'age':26, 'phone': '555-5555'})
del student['age']
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)