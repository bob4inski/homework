def palindrom(n):
    
    b = n[::-1]
    if n == b:
        return ('True')
    else:
        return ('False')

def Rashirenie(string:str):
    return string.split('.')[1]
    

def time(n):
    days = str(n  // 86400)
    n = n % 86400
    hours = str((n % 86400 ) // 3600)
    n = n % 3600
    minutes = str(n // 60)
    n = n % 60
    sek =str( n )
    return (days +':'+hours+':'+minutes+':'+sek)
    #print(days,':',hours,':',minutes,':',sek)

def Mnogo(n,k):
    b = n
    f = str(n)
    c = ''
    for i in range(2,k+1):
        g = f * i
        b += int(g)
    return(b)

        

    

print('введите строку ')
a = input()
print(palindrom(a))

print('введите файл')
b = input()
print(Rashirenie(b))

print('введите время')
c = int(input())
print(time(c))

print('введите число')
d = int(input())
print('введите количество повторов ')
k=int(input())
print(Mnogo(d,k))




    