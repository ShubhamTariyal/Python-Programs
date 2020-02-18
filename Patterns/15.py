'''

Output:
-------

Enter value:5
        A   
      A   B   
    A   B   C   
  A   B   C   D   
A   B   C   D   E 


'''

n = int(input('Enter value:'))
for i in range (n):
    for j in range(n):
        if i >= j - n + 1 and i + j >= n - 1:
            print(chr(ord('A') + i + j - n + 1),end='   ')
        else:
            print(end='  ')
    print()
