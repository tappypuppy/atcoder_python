H,W = map(int,input().split())

S = []

for i in range(H):
    S_i = input()
    S.append(S_i)

object1 = [-1,-1]
object2 = [-1,-1]

for i in range(H):
    for j in range(W):
        if (S[i][j] == 'o') and (object1 == [-1,-1]):
            object1 = [i,j]
        elif (S[i][j] == 'o') and (object2 == [-1,-1]):
            object2 = [i,j]


min_step = abs(object1[0] - object2[0]) + abs(object1[1] - object2[1])

print(min_step)

