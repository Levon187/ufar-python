def g():
    print("Start")
    x = 42
    yield x  # return x
    x = x + 1
    print('middle')
    yield x
    print("Finish")
    yield


gen = g()

print(type(gen))

result = next(gen)
print(result)
result = next(gen)
print(result)
result = next(gen)
print(result)
print(type(result))
# ////////////////////////

l = [5, 4, 6, 7, 8]

def process_list(l):
    maxi = max(l)
    yield maxi
    mini = min(l)
    yield mini


m = process_list(l)
print(next(m))
print(next(m))

# ////////////////////////

# big_list = [x**2 for x in range(10000000) if x%2 == 1]
# print(big_list[0:16])


big_gen = (x**2 for x in range(10000000) if x%2 == 1)
# big_list = list(big_gen)
print(big_gen)
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))
print(next(big_gen))