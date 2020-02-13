'''

Output:
-------

Enter value:5
        A   
      B   B   
    C   C   C   
  D   D   D   D   
E   E   E   E   E   


'''

n = int(input('Enter value:'))
for i in range (n):
    for j in range(n):
        if i >= j - n + 1 and i + j >= n - 1:
            print(chr(ord('A') + i),end='   ')
        else:
            print(end='  ')
    print()
