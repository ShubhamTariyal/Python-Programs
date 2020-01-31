'''

Output:

Enter value:7
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

n = int(input('Enter value:'))
for i in range (2*n - 1):
	for j in range(n):
		if i >= j and i + j <= 2*n - 2:
			print('*',end=' ')
	print()
