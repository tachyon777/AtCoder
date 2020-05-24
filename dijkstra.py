#AOJ GRL_1_A (ダイクストラ法テンプレート)
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,r = map(int,readline().split())
g = [[] for i in range(n)]
for i in range(m):
    x,y,w = map(int,readline().split())
    g[x].append((w,y))
    #g[y].append((w,x))

#新ダイクストラ
INF = 10**18
import heapq
push = heapq.heappush
pop = heapq.heappop
def dijkstra(s,g): #g:(weight,go)の順の隣接リスト※タプルで有ることに注意
    n = len(g)
    dist = [INF]*n
    dist[s] = 0
    used = [0]*n
    used[s] = 1
    hp = []
    for go in g[s]:
        push(hp,go)
    while hp:
        print(hp)
        w,fr = pop(hp)

        if not used[fr]:
            dist[fr] = w
            used[fr] = 1
            for w,go in g[fr]:
                if not used[go]:
                    push(hp,(w+dist[fr],go))
    
    return dist

for i in dijkstra(r,g):
    print(i if i < INF else "INF")