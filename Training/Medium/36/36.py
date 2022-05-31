def gcd(a,b): #関数を定義
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,X = map(int,input().split())

x = list(map(int, input().split()))

re_x = []

for loc in x:
    re_x.append(abs(loc - X))

re_x = list(set(re_x))

a = re_x[0]

for num in re_x:
    a = gcd(a,num)

print(a)