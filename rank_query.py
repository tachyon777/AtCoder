import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

#何番目に大きいかを同じリスト長で返す
#以下のように、n番目がかぶる場合、その次の順位のものはn+1番目としかできない
#重複を許さない場合、その下のnot_chohukuを適用する
#入力：[20,10,30,20]
#出力：[2,3,1,2] #1,2,2,3番目

#上位のものが重複している場合、下位をそのぶんずらす(not_chohuku())
#入力：[20,10,30,20]
#出力：[2,4,1,2] #1,2,2,4番目

#昇順(小さい順)モード：True
#入力：[20,10,30,20]
#出力：[2,1,3,2]

def rank(lst,syoujun=False):
    res2 = list(set(lst))
    ans = []
    if syoujun:
        res2.sort()
    else:
        res2.sort(reverse=True)
    dic1 = dict()
    for i in range(len(res2)):
        dic1[res2[i]] = i
    for i in lst:
        #ans.append(dic1[i]) #zero-indexed
        ans.append(dic1[i] + 1) #one-indexed
    
    return ans

def not_chohuku(lst): #rankで出力されたリストをそのまま入れれば下位ずらしを出力
    res = sorted(lst)
    dic1 = dict()
    count = 1
    now = 1

    if res[0] != res[1]:
        dic1[res[0]] = now

    for i in range(1,len(res)):
        if res[i] == res[i-1]:
            count += 1
        else:
            now += count
            dic1[res[i]] = now
            count = 1
    ans = []
    for i in lst:
        #zero-indexedはrank()に依存
        ans.append(dic1[i])
    return ans


#使用例1(not_chohuku() mode)
lst1 = list(map(int,readline().split()))
print(not_chohuku(rank(lst1))) #[2,4,1,2]

#使用例2 (ABC018-A 豆まき)
a = int(readline())
b = int(readline())
c = int(readline())
lst1 = [a,b,c]
ans = rank(lst1)
for i in ans:
    print(i)