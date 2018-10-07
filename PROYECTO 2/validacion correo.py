Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def valcor():
	z=0
	y=0
	x=0
	correo= str (input('correo...'))
	a= correo.find("@")
	b=correo.find('.')
	for i in range (0,(a)):
		if correo[i]=='@':
			x=x+1
	for j in range(0,len(formato)):
		if correo[(a+1):b]==formato[j]:
			y=y+1
			j=j+1
	for k in range (0,len(dominio)):
		if correo[(b+1):len(correo)]==dominio[k]:
			z=z+1
			k=k+1
	if y==0 or z==0 or x>=1:
		print('correo no valido')
	else:
		print('correo valido')

		
>>> formato=['hotmail','gmail','outlook','itnl','live']
>>> dominio=['com','edu','gob','mil','net','org']
>>> 
