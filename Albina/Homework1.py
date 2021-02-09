# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.


# a=int(input("Please enter an integer"))
# b=int(input("Please enter the second integer"))
# i=3
# def is_multiple(n, m):
#
#     if n%m==0:
#
#         return True
#     return  False
#
# print(is_multiple(a,b))


# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
# k = int(input("Enter a value to check if its even "))
# def is_even(k):
#     #TODO
#
#     if k%2 == 0:
#         return True
#     return False
#
# print(is_even(k))

'''def is_even(k):
    if k & 1:
        return False
    return  True

print(is_even(2))
print(is_even(3))

print(is_even())'''
# (-1)**k

# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

'''def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [5, 2, 3, 4, 5, 100, 7, 8, 99]

print(minmax(alpha))'''


# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

'''def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print('sum of squares')
print(sum_of_squares(4))'''


#Second version
'''def sum_square(n):
    result = 0
    if n > 0:
        for i in range(n):
            result += i * i
        return result
    elif n <= 0:
        return ("n should be positive")

print(sum_square(5))'''


# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
















