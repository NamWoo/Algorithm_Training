# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기 D2

# 20x10, 20x20, 20x??
T = 3
N = [30, 50, 70]
#1 5
#2 21
#3 85
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

for c, i in enumerate(N):
    a = ((i//20)*2) + 1
    a = ((i//20)*2) + 1
    b = 2**(i//20)
    print(b)
    print(f'#{c+1} {a}')
    print(f'#{c+1} {a}')


