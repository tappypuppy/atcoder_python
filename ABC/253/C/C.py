Q = int(input())

S = {}
S_set = set()

for i in range(Q):
    q = [_ for _ in input().split()]

    if q[0] == '1':
        x = int(q[1])
        if x in S_set:
            S[x] += 1
        else:
            S_set.add(x)
            S[x] = 1

    if q[0] == '2':
        x = int(q[1])
        c = int(q[2])
        
        if x in S_set:
            S[x] -= c
            if S[x] <= 0:
                S_set.remove(x)
                S.pop(x)
    
    if q[0] == '3':
        max_S = max(S)
        min_S = min(S)
        print(max_S - min_S)
