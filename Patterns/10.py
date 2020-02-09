'''

Output:
-------

Enter value:5
        E 
      E D 
    E D C 
  E D C B 
E D C B A 
  E D C B 
    E D C 
      E D 
        E 


'''

def prnt(k,n):
    for i in range (n-1,k-1,-1):
        print(chr(ord('A') + i),end=' ')
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
