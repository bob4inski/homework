def range_1(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number
        number += step
print(type(range_1))
ranger = range_1()
print(type(ranger))
for x in ranger:
    print(x)