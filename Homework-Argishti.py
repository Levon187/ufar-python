'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
def is_multiple(n, m):
    if n%m == 0:
        return True
    else:
        return False

'''
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''
def is_even(k):
    if k**-1 > 0:
        return True
    else:
        return False

'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
def minmax(data):
    max = min = data[0]
    for elem in data:
        if elem > max:
            max = elem
        else:
            min = elem
    max_min = (max, min)
    print(max_min)

'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''
def sum_of_squares(n):
    n -= 1
    sum = 0
    while n > 0:
        sum += n**2
        n -= 1
    return sum

'''
Give a single command that computes the sum from Exercise R-1.4, relying 
on Python’s comprehension syntax and the built-in sum function.
'''
def sum_of_squares_simple(n):
    return sum([k**2 for k in range(0, n)])

'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
def sum_of_squares_of_odds(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i*i
    return sum

'''
Give a single command that computes the sum from Exercise R-1.6, relying 
on Python’s comprehension syntax and the built-in sum function.
'''
def sum_of_squares_of_odds_simple(n):
    return sum([k**2 for k in range(1, n, 2)])

'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, 
what is the equivalent index j ≥ 0 such that s[j] references
the same element? 
'''
# answer: j = n + k, difference between j and k is always the length of the sequence

'''
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
'''

# answer:
# range(50, 81, 10):

'''
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
'''
# answer:
# range(8, -9, -2):

'''
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
'''

# answer: I can't and I don't want to copy here a code from internet :)

'''
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''
number = int(input("enter an integer which is greater than 2: "))
while number < 2:
    number = int(input("enter an integer which is greater than 2: "))

count = 0
while number > 2:
    number = number/2
    count = count + 1
# print(count)

'''
    NOTE: there are two exercises which I have not done, I will send them during the week
'''