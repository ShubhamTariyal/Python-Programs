'''

Output:
-------

Enter value:5
        1   
      1   2   
    1   2   3   
  1   2   3   4   
1   2   3   4   5  


'''

n = int(input('Enter value:'))
for i in range (n):
    for j in range(n):
        if i >= j - n + 1 and i + j >= n - 1:
            print(i + j + 1 - n + 1,end='   ')
        else:
            print(end='  ')
    print()
