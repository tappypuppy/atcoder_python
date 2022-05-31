A,B,X = map(int, input().split())

max_digit = 19

max_N = 0

for digit in range(1,max_digit+1):
    amari = X - B*digit

    if amari <= 0:
        break

    N = amari // A

    if N < 10**digit:
        max_N = max(max_N, N)
    else:
        max_N = max(max_N, (10**digit - 1))

if max_N > 10**9:
    print(10**9)
else:
    print(max_N)

