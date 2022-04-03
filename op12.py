def base2(n) :
    t = "0123456789ABCDEF"
    q,r = divmod(n,2)
    if q == 0:
        return t[r]
    else:
        return base2(q) +t[r]
#2021041032_정강훈
def base8(n) :
    t = "0123456789ABCDEF"
    q,r = divmod(n,8)
    if q == 0:
        return t[r]
    else:
        return base8(q) +t[r]

def base16(n) :
    t = "0123456789ABCDEF"
    q,r = divmod(n, 16)
    if q == 0:
        return t[r]
    else:
        return base16(q) + t[r]

n=0


if __name__=="__main__" :
    n = int(input('10진수 입력 --> '))
answer = base2(n)
answer2 = base8(n)
answer3 = base16(n)
print("2진수 : ", answer)
print("8진수 : ", answer2)
print("16진수 :",answer3)
