a = [1,3,6,3,23,3,45,54,56,67,34,233,13,1]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)