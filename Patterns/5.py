'''

Output:
-------

Enter value:5
E 
D E 
C D E 
B C D E 
A B C D E 
B C D E 
C D E 
D E 
E 


'''

def prnt(k,n):
	for i in range (k,n):
		print(chr(ord('A') + i),end=' ')
	print()

def pat(i,n):
	prnt(n-1-i,n)
	if i == n - 1 :
		return
	pat(i+1,n)
	prnt(n-1-i,n)

n = int(input('Enter value:'))
pat(0,n)
