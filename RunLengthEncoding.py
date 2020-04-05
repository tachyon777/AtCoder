#ランレングス符号化
"""
例：aabbbaad
出力：[[a,2],[b,3],[a,2],[d,1]]
"""
#例題(ABC019-B 高橋くんと文字列圧縮)
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

s = readline().rstrip().decode('utf-8')

#ランレングス符号化
def RLE(s):
    res = s[0]
    count = 0
    lst = []
    for i in s:
        if i == res:
            count += 1
        else:
            lst.append([res,count])
            count = 1
            res = i
    lst.append([res,count])

    return lst

lst1 = RLE(s)
ans = ""
for i,j in lst1:
    ans = ans + i + str(j)

print(ans)