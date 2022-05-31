import numpy as np

N = int(input())

h = list(map(int, input().split()))

max_h = max(h)

arr = np.zeros((N,max_h), dtype = int)

for i in range(N):
    for j in range(max_h):
        if h[i] >= j+1:
            arr[i][j] = 1


counter = 0

for j in range(max_h):
    i = 0
    num = -1
    while i < N:
        if (num != 1) and (arr[i][j] == 1):
            counter += 1
        
        num = arr[i][j]
        i += 1


print(counter)
