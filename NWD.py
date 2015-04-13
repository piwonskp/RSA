import sys

def NWD(a,b):
    u=1
    x=0
    while not a==b:
        if a>b:
            a=a-b
            u=u-x
        else:
            b=b-a
            x=x-u
    return [a,x] 

a=int(sys.argv[1])
b=int(sys.argv[2])
w=NWD(a, b)

print 'NWD:',w[0]
if w[0]==1
    print 'liczba odwrotna do', a, 'modulo', b, 'to', w[1]+b
