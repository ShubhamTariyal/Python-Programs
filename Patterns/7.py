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

def prnt(k,n):
    for i in range (n-1,k-1,-1):
        print(i,end=' ')
    print()

def pat(i,n):
    space(n - 1 - i)
    prnt(n-1-i,n)
    if i == n - 1 :
        return
    pat(i+1,n)
    space(n - 1 - i)
    prnt(n-1-i,n)

def space(n):
    for i in range(n):
        print(end='  ')

n = int(input('Enter value:'))
pat(0,n)

