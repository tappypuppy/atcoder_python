T = int(input())

def yakusu(l):
    div = []
    for i in range(1, l):
        if l % i == 0:
            div.append(i)
    
    return div

for _ in range(T):
    case = input()

    if len(case) == 2:
        case_int = int(case)
        print((case_int // 11)*11)
    
    if len(case) >= 3:
        N = int(case)
        k = len(case)
        max_num = 0

        #1 k-1
        max_num = max(max_num, 10**(k-1) - 1)

        # Nd, Nd-1
        div = yakusu(k)

        for d in div:
            a = case[0:d]
            a_str = str(a)
            Nd = int(a_str*(k//d))
            if Nd > N:
                m = int(str(a)) - 1
                if m > 0:
                    Nd1 = int(str(m)*(k//d))
                    max_num = max(max_num,Nd1)
            else:
                max_num = max(max_num,Nd)
        
        print(max_num)


