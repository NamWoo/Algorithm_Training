T = int(input())
N  = []
# 입력
for i in range(T):
    Nc = list(map(int, input().split()))
    N.append(Nc)

# 연산
fac = 1
for count, i in enumerate(N):
    for j in range(1, 1+i[0]):
        fac *= j    

    c, d = max(fac, i[1]), min(fac, i[1])
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    
    # 출력
    print(f'#{count+1} {c}')





