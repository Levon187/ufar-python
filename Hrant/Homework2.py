'''1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m'''
def is_multiple(n, m):
    if m == 0:
        return "ZERO DIVISION ERROR"
    if n % m == 0:
        return True
    return False


'''1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise'''
def is_even(k):
    while k >= 2:
        k -= 2
    if k == 0:
        return True
    return False


'''1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. '''
def minmax(listt):
    min_el = listt[0]
    max_el = listt[0]
    for elem in listt:
        if min_el > elem:
            min_el = elem
        if max_el < elem:
            max_el = elem
    return min_el, max_el


'''1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n'''
def pos_sqr(n):
    if n <= 0:
        return "ERROR, SHOULD BE POSITIVE"
    sum = 0
    for i in range(1, n):
        sum += i ** 2
    return sum


'''1.5 Give a single command that computes the sum from Exercise 
R-1.4, relying on Python’s comprehension syntax and the built-in sum function.'''
def pos_sqr_com(n):
    if n <= 0:
        return "ERROR, SHOULD BE POSITIVE"
    return sum([i ** 2 for i in range(1, n)])


'''1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''
def sqr_odd(n):
    if n <= 0:
        return "ERROR, SHOULD BE POSITIVE"
    sum = 0
    for i in range(1, n, 2):
        sum += i ** 2
    return sum


'''1.7 Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function'''
def sqr_odd_com(n):
    if n <= 0:
        return "ERROR, SHOULD BE POSITIVE"
    return sum([i ** 2 for i in range(1, n, 2)])



