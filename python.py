def seksem(f,g):
    seksem = f+ g
    if f>g:
        print('seksem ki mkc')
    else:
        seksem(f+1, g)
        return seksem
a = int(input())            
b = int(input())
print(seksem(a,b))