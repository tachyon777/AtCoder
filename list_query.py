class list_query():
    """
    リストに対する様々な変形を行うクラス
    欲しい機能が追加されるたびに更新する予定。
    """
    def __init__(self,lst):
        self.l = len(lst)
        self.lst = lst
    
    #i番目をxに変更
    def update(self,i,x):
        self.lst[i] = x

    #単調増加/減少個数のリスト(narrow:狭義に変更)
    #inc:[4,3,1,7]→[1,1,1,2]
    #dec:[4,3,1,7]→[1,2,3,1]
    #revinc:[4,3,1,7]→[3,2,1,1]
    #revdec:[4,3,1,7]→[1,1,2,1]
    def inc_dec(self,mode="inc",rev=False,narrow=False):
        lst2 = []
        res = 0
        if rev:
            self.lst = self.lst[::-1]
        if mode == "inc":
            last = -10**18
            if narrow:
                for i in self.lst:
                    if i > last:
                        res += 1
                        lst2.append(res)
                    else:
                        res = 1
                        lst2.append(res)
                    last = i
            else:
                for i in self.lst:
                    if i >= last:
                        res += 1
                        lst2.append(res)
                    else:
                        res = 1
                        lst2.append(res)
                    last = i
        elif mode == "dec":
            last = 10**18
            if narrow:
                for i in self.lst:
                    if i < last:
                        res += 1
                        lst2.append(res)
                    else:
                        res = 1
                        lst2.append(res)
                    last = i
            else:
                for i in self.lst:
                    if i <= last:
                        res += 1
                        lst2.append(res)
                    else:
                        res = 1
                        lst2.append(res)
                    last = i
        else:raise Exception
        if rev:
            self.lst = self.lst[::-1]
            lst2 = lst2[::-1]
        return lst2