import os
from datetime import datetime

"""
#print(dir(os))

print(os.getcwd())

os.chdir('/home/neila/code/SEII-NeilaCristinaMoraisSilva/')
print(os.getcwd())

print(os.listdir())

os.chdir('/home/neila/Documents/')
os.mkdir('os-demo-1')
print(os.listdir())

os.makedirs('os-demo-2/subdir-demo-1')
print(os.listdir())

os.rmdir('os-demo-1')
os.removedirs('os-demo-2/subdir-demo-1')
print(os.listdir())

'''os.rename('teste.txt', 'demo.txt')
print(os.listdir())'''

print(os.stat('demo.txt'))

print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)

from datetime import datetime
mo_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mo_time))
"""

os.chdir('/home/neila/Documents/')
for dirpath, dirnames, filename in os.walk('/home/neila/Documents/'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filename)
	print()

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('/temp/test.txt'))
print(os.path.split('/temp/test.txt'))

print(os.path.exists('/temp/test.txt'))

print(os.path.isdir('/home/neila/Documents/'))
print(os.path.isfile('/home/neila/Documents/'))

print(os.path.splitext('/temp/test.txt'))

print(dir(os.path))
