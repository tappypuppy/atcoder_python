N = input()

N_int = int(N)

#4 : 1, 7:2, 10: 3, 13:4

N_size = len(N)

if N_size < 4:
    print(0)

if N_size >= 4 and N_size <7:
    ans = N_int - 10**3 + 1
    print(ans)

if N_size >=7 and N_size < 10:
    comma_1 = 10**6 - 10**3
    comma_2 = (N_int - 10**6 + 1)*2

    ans = comma_1 + comma_2
    print(ans)

if N_size >= 10 and N_size < 13:
    comma_1 = 10**6 - 10**3
    comma_2 = (10**9 - 10**6)*2
    comma_3 = (N_int - 10**9 + 1)*3
    
    ans = comma_1 + comma_2 + comma_3
    print(ans)

if N_size >= 13 and N_size < 16:
    comma_1 = 10**6 - 10**3
    comma_2 = (10**9 - 10**6)*2
    comma_3 = (10**12 - 10**9)*3
    comma_4 = (N_int - 10**12 + 1)*4

    ans = comma_1 + comma_2 + comma_3 + comma_4
    print(ans)

if N_size >= 16 :
    comma_1 = 10**6 - 10**3
    comma_2 = (10**9 - 10**6)*2
    comma_3 = (10**12 - 10**9)*3
    comma_4 = (10**15 - 10**12)*4
    comma_5 = (N_int - 10**15 + 1) * 5

    ans = comma_1 + comma_2 + comma_3 + comma_4 + comma_5
    print(ans)
