N,K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


max_value = 0

for value in A:
    max_value = max(value, max_value)

index = []

for idx in range(N):
    if A[idx] == max_value:
        index.append(idx+1)

flag = False

not_like = set(index) & set(B)

if not_like:
    print("Yes")
else:
    print("No")

