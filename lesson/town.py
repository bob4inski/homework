import random
def HEPON(count_pupils,count_size):
    
    
    return {'count_pupils':count_pupils,'count_size':count_size }
print()

def create_region(names,cities):
    d = {}
    for name,city in zip(names,cities):
        d[name] = city
    return d

cities = [HEPON(random.randrange(50),random.randrange(50)) for _ in range(50)]
names = [(random.randrange(50),random.randrange(50)) for _ in range(50)]
print(create_region(names,cities))