def hellofunc():
	pass
print(hellofunc)
print(hellofunc())

def hellofunc():
	print('Hello function!')
hellofunc()

def hellofunc():
	return'Hello function!'
print(hellofunc())

print(hellofunc().upper())

def hellofunc(greeting):
	return'{} function!'.format(greeting)
print(hellofunc('Hi'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}.'.format(greeting, name)
print(hellofunc('Hi'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}.'.format(greeting, name)
print(hellofunc('Hi', 'Neila'))

def hellofunc(greeting, name = 'You'):
	return '{}, {}.'.format(greeting, name)
print(hellofunc('Hi', name = 'Neila'))

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
student_info('math', 'art','compsci', name='john', age=25)

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
courses = ['math', 'art','compsci']
info = {'name':'john', 'age':25}
student_info(courses, info)

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
courses = ['math', 'art','compsci']
info = {'name':'john', 'age':25}
student_info(*courses, **info)
