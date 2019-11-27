import sys

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

list = sys.argv[1:]
n = len(list)
print(n)
k = 1
while k < n:
    j = 0
    while j <= n-2:
        if int(list[j]) > int(list[j+1]):
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp 
        j += 1
    k += 1    
print(list)    