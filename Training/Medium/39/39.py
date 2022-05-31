K,A,B = map(int, input().split())

bis = 1

if K < A+1: # K_res = K - (A-1) < 2
    bis += K
else:
    if B - A > 2:
        K_res = K - (A-1)
        bis += A - 1
        if K_res % 2 == 1:
            bis += 1
            K_res -=1
        
        bis += (K_res // 2) * (B-A)
    else:
        bis += K

print(bis)
