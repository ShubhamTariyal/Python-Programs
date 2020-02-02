'''

Output:
-------

Enter value:5
4 
3 4 
2 3 4 
1 2 3 4 
0 1 2 3 4 
1 2 3 4 
2 3 4 
3 4 
4 


'''

def prnt(k,n):
	for i in range (k,n):
		print(i,end=' ')
	print()
def pat(i,n):
	prnt(n-1-i,n)
	if i == n - 1 :
		return
	pat(i+1,n)
	prnt(n-1-i,n)
n = int(input('Enter value:'))
pat(0,n)

