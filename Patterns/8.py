'''

Output:
-------

Enter value:7
            6 
          5 6 
        4 5 6 
      3 4 5 6 
    2 3 4 5 6 
  1 2 3 4 5 6 
0 1 2 3 4 5 6 
  1 2 3 4 5 6 
    2 3 4 5 6 
      3 4 5 6 
        4 5 6 
          5 6 
            6 


'''

def prnt(k,n):
    for i in range (k,n):
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
