'''

Output:
-------

Enter value:6
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2 1 0 
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 

'''
n = int(input('Enter value:'))
for i in range (2*n - 1):
	for j in range(n):
		if i >= j and i + j <= 2*n - 2:
			print(n-j-1,end=' ')
	print()
