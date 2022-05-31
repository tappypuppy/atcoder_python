N,W = map(int, input().split())

A = list(map(int, input().split()))


good_int = set()

for i in range(N):

    if A[i] <= W:
        good_int.add(A[i])
    
    if i<N-1:
        for j in range(i+1, N):

            if A[i] + A[j] <=W:
                good_int.add(A[i]+ A[j])
            
            if j<N-1:
                for k in range(j+1,N):

                    if A[i] + A[j] + A[k] <=W:
                        good_int.add(A[i]+ A[j] + A[k])


ans = len(good_int)

print(ans)