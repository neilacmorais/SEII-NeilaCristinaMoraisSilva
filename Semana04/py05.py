student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(student)

print(student['name'])
print(student['courses'])

student = {1:'John', 'age':25, 'courses': ['math', 'compsci']}
print(student[1])

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(student['name'])
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'not found'))

student['phone'] = '555-555'
print(student.get('phone', 'not found'))

student['name'] = 'Jane'
print(student)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(student)
student.update({'name':'Jane', 'age':26, 'phone':'555-555'})
print(student)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(student)
del student['age']
print(student)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(student)
age = student.pop('age')
print(student)
print(age)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
print(len(student))

print(student.keys())

print(student.values())

print(student.items())

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
for key in student:
	print(key)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
for key, value in student.items():
	print(value)

student = {'name':'John', 'age':25, 'courses': ['math', 'compsci']}
for key, value in student.items():
	print(key, value)
