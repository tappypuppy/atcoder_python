import math

N,A,B = map(int,input().split())


def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)


lcm = my_lcm(A,B)

A_sum = 0
B_sum = 0
lcm_sum = 0

ma = N // A
A_sum += int((ma*(ma+1))/2)*A

ma = N // B
B_sum += int((ma*(ma+1))/2)*B



ma = N // lcm
lcm_sum += int((ma*(ma+1))/2)*lcm



AB_sum = A_sum + B_sum - lcm_sum
N_sum = (N*(N+1)) // 2

ans = N_sum - AB_sum

print(ans)
