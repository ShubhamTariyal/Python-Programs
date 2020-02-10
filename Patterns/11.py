'''

Output:
-------

Enter value:5
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   * 


'''

n = int(input('Enter value:'))
for i in range (n):
    for j in range(n):
        if i >= j - n + 1 and i + j >= n - 1:
            print('*',end='   ')
        else:
            print(end='  ')
    print()
