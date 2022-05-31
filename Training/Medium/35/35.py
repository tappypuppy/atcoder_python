def gcd(a,b): #関数を定義
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    gcd_num = gcd(a,b)
    return (a * b) // gcd_num

def f(x,c,d):
    cd_lcm = x // lcm(c,d)
    c_count = x // c
    d_count = x // d

    count = c_count + d_count - cd_lcm

    if c == d:
        return x - (x // c)
    else:
        return x - count

        

A,B,C,D = map(int,input().split())


ans = f(B,C,D) - f(A-1,C,D)

print(ans)