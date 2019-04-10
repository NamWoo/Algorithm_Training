T = int(input())
for i in range(T):
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))

    initt = N[0]
    flag = 0
    flagelse = 0

    while initt < N[1]:
        # print(initt)
            
        if initt in M:      
            # print('aa', initt)
            flag = flag + 1 
            initt = initt + N[0]
            # print('ac', initt, flag)
        else:
            # print('bb', initt)
            initt = initt - 1
            flagelse = flagelse + 1
            # print('bc', initt, 'flagelse',flagelse)
        if flagelse == N[0]:
            flag = 0
            break
        

    print(f'#{i+1} {flag}')