def gen_names(name,num):
    i = 1 
    while i < num:
        yield name 
        i += 1
ranger = gen_names('Роберто',100)
names = [x for x in ranger]
print(names)