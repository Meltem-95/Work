Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci(i):
	if i<0:
		print("Please enter natural number")
	elif i==0:
		return 0
	elif i==1:
		return 1
	else:
		return fibonacci(i-1)+fibonacci(i-2)

	
>>> fibonacci(7)
13
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(6)
8
>>> 
