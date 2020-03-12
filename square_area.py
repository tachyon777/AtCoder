class Square_area():
    """
    about:
    四角形の左縁からx1,右縁からx2迄,下縁からy1迄,上縁からy2迄,塗りつぶした時の、塗りつぶした面積を出力する。
    require:
    w,h,x1,x2,y1,y2
    w:幅
    h:高さ
    四角形の左下の座標を(0,0)とした時、
    x1:その左側を塗りつぶす
    x2:その右〃
    y1:その下〃
    y2:その上〃
    x1とx2の領域が重なる(x2<x1)の場合は、全て塗りつぶすという扱いになる。yについても同様。
    """
    def __init__(self,w,h,x1,x2,y1,y2): #塗りつぶさないなら:(x1=0,x2=w,y1=0,y2=h)
        self.w = w
        self.h = h
        self.area = w*h
        self.x1 = x1
        if x2 < x1:
            self.x2 = w-x1
        else:
            self.x2 = w-x2
        self.y1 = y1
        if y2 < y1:
            self.y2 = h-y1
        else:
            self.y2 = h-y2
        
        for i in [self.x1,self.x2]:
            if not 0 <= i <= w:
                raise Exception
        for i in [self.y1,self.y2]:
            if not 0 <= i <= h:
                raise Exception

    def get_outer(self): #指定した座標の外側の面積
        return (self.x1+self.x2)*self.h +(self.y1+self.y2)*self.w - self.dublication()

    def get_inner(self): #指定した座標の内側の面積
        return self.area - self.get_outer()

    def dublication(self): #重複部分の面積。x同士、y同士の重複はinitで処理してしまっているので注意
        return self.x1*(self.y1+self.y2)+self.x2*(self.y1+self.y2)