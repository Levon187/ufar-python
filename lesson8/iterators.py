numbers = [2, 5, 4, 6, 7]


def power(n):
    return n**2


new_numbers = []

for number in numbers:
    new_numbers.append(power(number))

# print("__iter__" in numbers.__dir__())
# n1 = 5
# print("------------------------")
# print("__iter__" in n1.__dir__())

it = iter(numbers)

while True:
    try:
        x = next(it)
    except StopIteration:
        break
    new_numbers.append(power(x))

print(new_numbers)



print(list(range(20))[10])   #  this created 20-elemnt list from 0 to 19 and prints the 10-th element

print((range(20)[10]))     # this runs next() 10 times to get the element instead of 20 times