Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> def kmp():
	cadena=(input('cadena...'))
	patron=(input('patron...'))
	print("se obtiene '"+patron+"' en: ")
	for i in range (0,len(cadena)):
			c=cadena[i:(len(cadena)+i)]
			d=re.match(patron,c)

			if bool(d)==True:
				 print(i)
			i=i+1

			
>>> 
