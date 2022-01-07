"""
try:
	f = open('teste.txt')
except Exception:
	print('Sorry. This file does not Exist.')"""

"""
try:
	f = open('teste.txt')
	var = bar_bad
except FileNotFoundError:
	print('Sorry. This file does not Exist.')
except Exception:
	print('Sorry. Something went wrong.')
	"""



try:
	f = open('py02.py')
except FileNotFoundError as error:
	print(error)
except Exception as error:
	print(error)
else:
	print(f.read())
	f.close()
finally:
	print('Executing Finally....!!')
