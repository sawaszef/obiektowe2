def gen_int(i=1):
    while True:
        yield i
        i += 1

def gen_square(i=1):
    for n in gen_int(i):
        yield n**2

def select(iter_obj, n):
    obj_list = []
    for _ in range(n):
        obj_list.append(next(iter_obj))
    return obj_list

def pythagoras(limit = 50):
    for a in range(1, limit):
        for b in range(a + 1, limit):
            for c in range(b + 1, limit):
                if c ** 2 == a ** 2 + b ** 2:
                    yield (a, b, c)





test_list = select(pythagoras(), 15)
print(test_list)
