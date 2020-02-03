'''

Output:
-------

Enter value:6
F 
F E 
F E D 
F E D C 
F E D C B 
F E D C B A 
F E D C B 
F E D C 
F E D 
F E 
F 


'''

n = int(input('Enter value:'))
for i in range (2*n - 1):
	for j in range(n):
		if i >= j and i + j <= 2*n - 2:
			print(chr(ord('A') + n - 1 - j),end=' ')
	print()
