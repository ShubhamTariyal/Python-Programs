'''

Output:
-------

Enter value:6
          5 
        4 5 
      3 4 5 
    2 3 4 5 
  1 2 3 4 5 
0 1 2 3 4 5 
  1 2 3 4 5 
    2 3 4 5 
      3 4 5 
        4 5 
          5 


'''

n = int(input('Enter value:'))
for i in range (2*n - 1):
    for j in range(n):
        if i <= j + n - 1 and i + j >= n - 1:
            print(chr(ord('A') + j),end=' ')
        else:
            print(end='  ')
    print()
