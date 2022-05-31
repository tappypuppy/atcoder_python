# for ma in range(1000):
#     for A in range(10000):
#         A_int = int((ma*(ma+1))/2)*A
#         A_sum = ((ma*(ma+1))//2)*A
#         if A_int != A_sum:
#             print(ma,A,A_int,A_sum)

for ma in range(10**9+1):
    A_int = int((ma*(ma+1))/2)
    A_sum = (ma*(ma+1))//2
    
    if A_int != A_sum:
        print(ma,A_int,A_sum)