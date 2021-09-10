def piramidka(n):

    pir  = []
    #if n % 2 ==0:
    g = int(n // 2)+1
    pir = [] * g
    print(g)
    dl = n 
    i = 0
    for hh in range(g):
        pirr= ' '*hh + '*'*(dl-hh*2) + ' '*hh
        pir.append(pirr)
    
    return pir[::-1]

        
    

i = int(input())
mass = piramidka(i)

for g in range(len(mass)):
    print(mass[g])






    
        