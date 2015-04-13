import sys

def power(m,f,n):
    f=format(f,'08b')
    product=1
    i=m
    for bit in reversed(f):
        if bit == '1':
            product=product*i%n
        i=i*i%n
    return product


m=int(sys.argv[1])
f=int(sys.argv[2])
n=int(sys.argv[3])
print power(m,f,n)
