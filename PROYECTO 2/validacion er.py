Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> 
def validacionc():
	correo=str(input('correo...'))
	x=0
	a=correo.find('@')
	b=correo.find('.com')
	for i in range (0,a):
		c=correo[i]
		d=re.match('[a-z0-9A-Z-_.]',c)
		if bool(d)==False:
			x=x+1
	for j in range((a+1),b):
		e=correo[j]
		f=re.match('[a-z]',e)
		if bool(f)==False:
			x=x+1
	if bool(a)==False or bool(b)==False or x>=1:
		print('correo no valido')
	else:
		print('correo valido')

		
>>> 
