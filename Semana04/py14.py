import os

os.chdir('/home/neila/Documents/py12/')
print(os.getcwd())

for f in os.listdir():
	#print(f)
	#print(os.path.splitext(f))
	file_name, file_ext = os.path.splitext(f)
	#print(file_name)
	
	file_title, file_corse, file_num = file_name.split('-')
	#print(file_num)
	
	file_num = file_num.strip()[1:].zfill(2)
	file_title = file_title.strip()
	file_corse = file_corse.strip()
	
	print(f'{file_num}-{file_corse}-{file_title}{file_ext}')
	
	new_name = '{}-{}-{}{}'.format(file_num, file_corse, file_title, file_ext)
	
	os.rename(f, new_name)
