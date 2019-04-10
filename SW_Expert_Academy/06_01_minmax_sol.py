T = int(input())
lineby = {}
for i in range(T):
    N = int(input())
    aj = list(map(int, input().split()))
    lineby[i] = aj

# print(lineby)

for i in lineby:
    a = max(lineby[i]) - min(lineby[i])
    print(f'#{i+1} {a}')
