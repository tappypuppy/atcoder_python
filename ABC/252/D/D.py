from collections import defaultdict
N = int(input())

A = list(map(int,input().split()))

max_combo = N*(N-1)*(N-2)/(3*2)

value_counts = defaultdict(lambda:0)

for v in A:
    value_counts[v] += 1

del_combo = 0

A_set = list(set(A))

for v in A_set:
    c = value_counts[v]
    if c >= 3:
        #dup3
        del_combo += c*(c-1)*(c-2)/6
        #dup2
        possible_combo = c*(c-1)/2
        del_combo += possible_combo*(N-c)

    if c == 2:
        #dup2
        del_combo += N-c


ans = int(max_combo - del_combo)

print(ans)


