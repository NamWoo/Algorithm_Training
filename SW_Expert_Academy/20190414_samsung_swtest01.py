# 브루트포스, dfs, bfs, 구현시뮬레이션
from operator import itemgetter, attrgetter
import operator

T = 10
N = 4, 6
abbo = [[2,3,3],[3,1,1],[1,2,3]]
new = {}
bmax = 0

for i in abbo:  
    for j in set(i):
        ic = i.count(j)
        new[j] = ic 

        
        newnew = sorted(new.items(), key=operator.itemgetter(1))

        print(newnew)