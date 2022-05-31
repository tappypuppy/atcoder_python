N = int(input())
A = list(map(int, input().split()))

B1 = 0

for i in range(N):
    if i % 2 == 0:
        B1 += A[i]
    else:
        B1 -= A[i]

B = [B1]

for i in range(1,N):
    B_i = 2*A[i-1] - B[i-1]
    B.append(B_i)

print(*B)