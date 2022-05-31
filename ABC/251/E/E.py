import queue
from re import A
import re

step = int(input())


#step 1
if step == 1:
    M = int(input())
    DSP = [map(int, input().split()) for _ in range(M)]
    D,S,P = [list(i) for i in zip(*DSP)]

    try:
        while True:
            O, T,D_C,N = input().split()
            if O == '':
                break

            T = int(T)
            D_C = int(D_C)
            N = int(N)

            # print(T,D_C,N)

            for i in range(M):
                if D[i] == D_C:
                    if S[i] >= N:
                        S[i] -= N

                        for n_order in range(N):
                            print("received order", T,D_C)
                    else:
                        print("sold out", T)
        
    except EOFError:
        pass



if step == 2:
    M,K = map(int, input().split())
    DSP = [map(int, input().split()) for _ in range(M)]
    D,S,P = [list(i) for i in zip(*DSP)]

    counter = 0

    que = []

    cooking_list = []

    try:

        while True:
            messege = input()

            if "received order" in messege:
                R,O, T, D_C = messege.split()
                T = int(T)
                D_C = int(D_C)

                if(counter <K):
                    counter +=1
                    cooking_list.append(D_C)
                    print(D_C)
                else:
                    print("wait")
                    que.append(D_C)
            
            if "complete" in messege:
                R, D_C = messege.split()
                D_C = int(D_C)

                exist_check = False

                for cooking_D in cooking_list:
                    if cooking_D == D_C:
                        exist_check = True
                
                if exist_check:
                    cooking_list.remove(D_C)
                    counter -= 1

                    if que:
                        cooking_list.append(que[0])
                        print("ok", que[0])
                        que.pop(0)
                        counter += 1
                    else:
                        print("ok")
                
                else:
                    print("unexpected input")
                    



    
    except EOFError:
        pass


if step == 3:
    M = int(input())

    DSP = [map(int, input().split()) for _ in range(M)]
    D,S,P = [list(i) for i in zip(*DSP)]

    cooking_list = []
    
    try:

        while True:
            messege = input()

            if "received order" in messege:
                R,O, T, D_C = messege.split()
                T = int(T)
                D_C = int(D_C)

                for i in range(M):
                    if D[i] == D_C:
                        if S[i] > 0:
                            cooking_list.append([T,D_C])
                            S[i] -= 1
            
            if "complete" in messege:
                R, D_C = messege.split()
                D_C = int(D_C)

                for ready_T, ready_D in cooking_list:
                    if ready_D == D_C:
                        print("ready", ready_T,ready_D)
                        cooking_list.remove([ready_T,ready_D])
                        break

    
    except EOFError:
        pass
