N = int(input())

S = []

for _ in range(N):
    S.append(input())

num = ["0","1", "2","3", "4","5","6","7","8","9"]

min_t = 100000

for stop_num in num: #止める番号
    t = 0
    for n_reel in range(10): #止める番号の位置
        counter = 0
        for S_i in S:
            if S_i[n_reel] == stop_num:
                counter += 1
        
        if counter == 0:
            max_t = 0
            t = max(t,max_t)
        else:
            max_t = n_reel + 10*(counter -1)
            t = max(t,max_t)

    min_t = min(t,min_t)

print(min_t)
