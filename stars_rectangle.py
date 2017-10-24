n = int(input())
for i in range(0, n):
    if i is 0 or i is (n - 1):
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')
