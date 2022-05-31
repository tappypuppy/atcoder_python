N = int(input())

Dup_check = set()

max_val = 0
ans = 0

for i in range(N):
    S,T = input().split()
    T = int(T)

    if S not in Dup_check:
        Dup_check.add(S)
        if max_val < T:
            max_val = T
            ans = i+1

print(ans)





