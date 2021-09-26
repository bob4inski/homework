def F(n,f):
    c = n 
    h =''
    while c > 0:
        h +=str(c%f)
        c = c // f 
    return h[::-1]

a = int(input())
b = int(input())
print(F(a,b))