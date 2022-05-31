from collections import defaultdict
from email.policy import default

N = int(input())

D = list(map(int, input().split()))

M = int(input())

T = list(map(int, input().split()))

test_dict = defaultdict(int)

for D_i in D:
    test_dict[D_i] += 1

flag = True

for T_i in T:
    if test_dict[T_i] >= 1:
        test_dict[T_i] -= 1
    else:
        flag = False

if flag:
    print("YES")
else:
    print("NO")