def query(l,r,c):
    l -=1
    r -=1

    ball_list = c[l:r+1]
    color_count = len(set(ball_list))
    return color_count

N,Q = map(int, input().split())

c = list(map(int, input().split()))

c_set_list = []

for i in range(N):
    c_i_set = set(c[:i+1])
    c_set_list.append(c_i_set)

for _ in range(Q):
    l,r = map(int, input().split())
    c_l = c_set_list[l-1]
    c_r = c_set_list[r-1]

    c_lr = c_l and c_r
    