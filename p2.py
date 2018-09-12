Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> alfabeto = ('a','b','c','d','e')
>>> def alfa(alfabeto):
	n=int(input('cantidad'))
	z=0
	a=3
	cadena = ""
	while z<n:
		z=z+1
		for i in range(1,a):
			cadena = cadena + alfabeto[random.randint(0,5)]
		print(cadena)
		cadena= ""

		
>>> import random
>>> 
