import random
import string

"""
REの原因が分からない際や、問題の法則性を探る際にデバッガーとして有用です。
input関数の代わりにtestcase関数を使用してください。
２行以上に渡って同じ入力を行う際、for文でinputを回してください。
入力をprintして確認したい場合はprint_modeをTrueにしてください。
"""

print_mode = True

def return_type(l,space):
    s = ""
    if space:
        s = " "
    if type(l[0]) == str:
        if print_mode:
            print(s.join(l))
        return s.join(l)
    else:
        if print_mode:
            print(s.join(map(str,l)))
        return s.join(map(str,l))

def integers(num=1,minint=1,maxint=10**5,space=True):
    #引数：返す整数の数、整数の最小値、最大値、スペースを入れて返すか否か
    lst = []
    for i in range(num):
        lst.append(random.randint(minint,maxint+1))
    
    return return_type(lst,space)

def strings(num=1,length=1,capitalize_mode=0,space=True):
    #引数：文字列の数、文字の長さ、大文字小文字モード、スペースを入れて返すか否か
    #capitalize_mode:0:全て小文字,1:全て大文字,2:ランダム
    lst = []
    if capitalize_mode == 0:
        for i in range(num):
            lst.append("".join([random.choice(string.ascii_lowercase) 
            for k in range(length)]))

    elif capitalize_mode == 1:
        for i in range(num):
            lst.append("".join([random.choice(string.ascii_uppercase) 
            for k in range(length)]))

    elif capitalize_mode == 2:
        for i in range(num):
            lst.append("".join([random.choice(string.ascii_lowercase+string.ascii_uppercase) 
            for k in range(length)]))
    else:
        print("capitalze_mode error")
        exit()
    return return_type(lst,space)


def maze(width=10,wall="#",road=".",space=False):
    #引数：(高さはforループの回数に依存)、幅、壁の文字、道の文字、スペースを入れて返すか否か
    #まじでRE用にしか使えないと思う
    lst = []
    for i in range(width):
        lst.append(random.choice([wall,road]))
    return return_type(lst,space)