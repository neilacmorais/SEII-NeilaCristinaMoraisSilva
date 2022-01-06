f = open('py02.py', 'r')

print(f.name)
print(f.mode)

f.close()

with open('py02.py', 'r') as f:
	pass
print(f.closed)

with open('py02.py', 'r') as f:
	#f_content = f.read()
	#print(f_content)
	'''f_content = f.readlines()
	print(f_content, end='')
	f_content = f.readline()
	print(f_content, end='')
	f_content = f.readline()
	print(f_content, end='')
	
	for line in f:
		print(line, end='')'''
	
	'''
	f_content = f.read(100)
	print(f_content)
	
	print(f.tell())'''
	
	'''f_content = f.read(10)
	print(f_content)
	
	f.seek(0)
	
	f_content = f.read(10)
	print(f_content)'''
	
'''with open('test.txt', 'w') as f:
	f.write('test')
	f.write('test')
	f.seek(0)
	f.write('hellooooo')'''

'''with open('test.txt', 'r') as rf:
	with open('testcopy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)'''

