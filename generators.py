import string 
def F(n):
    for i in range(len(n)):
        print(n[i])

def F2(n):
    a = len(n)
    d = 0 
    while d < a:
        print(n[d])
        d += 1





print(list(string.ascii_lowercase))

spisok = [chr(i) for i in range(97,123)]

'''for i in range(97,123):
    a = chr(i)
    spisok.append(a)
print(spisok)'''



i = 97
spisok1 = []
while i < 123:
    
    a = chr(i)
    spisok1.append(a)
    i += 1
print(spisok1)
print('1')

F(spisok)
print()
F2(spisok)
