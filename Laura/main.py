# 1.1-Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
# from numpy.core import number

def is_multiple(n, m):
    return bool(n % m)


# if n%m==0:
#  return false
# else:
#  return true

print(is_multiple(4, 4))


# 1.2-Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators
def is_even_func(k):
    if k[-1] != 0 or 2 or 4 or 6 or 8:
        return True
    else:
        return False


# is_even_func()

# 1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    data.sort()
    return data[0], data[-1]


arr = [4, 5, 11, 46, 78, 2, 6, 51]
print(minmax(arr))


# 1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def posi(num6):
    sums = 0
    while num6 > 0:
        num6 -= 1
        sums += num6 ** 2
    return sums


print(posi(8))


# 1.5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
def sum_one_line(num2):
    sum(i ** 2 for i in range(num2))


# 1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def posivodd(number1):
    sumsodd = 0
    if number1 > 0:
        number = number1 - 1
        if number % 2 == 1:
            sumsodd += number1 ** 2
    return sumsodd


# 1.7 Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.
def sum_odd_square(num4):
    sum(i ** 2 for i in range(1, num4, 2))


# 1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

# ??


# 1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

range(50, 90, 10)

# 1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

print(range(8, -10, -2))

# 1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

#??


# 1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

num_30 = input(int("Enter the number greater than 2 "))
sum_divide_2 = 0
if num_30 < 2:
    print("enter number greater than 2 ")
else:
    while num_30 < 2:
        num_30 %= 2
        sum_divide_2 += 1

# 1.32 Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.

num1 = input(float("Enter the first number "))
num2 = input(float("Enter the first number "))
calculate_operator = input("Enter the operator ")
if calculate_operator is '+':
    print(f"{num1}+{num2}={num1 + num2}")
elif calculate_operator is '-':
    print(f"{num1}-{num2}={num1 - num2}")
elif calculate_operator is '*':
    print(f"{num1}*{num2}={num1 * num2}")
elif calculate_operator is '/':
    if num2 != 0:
        print(f"{num1}*{num2}={num1 / num2}")
    else:
        print("We cannot divide number on 0")
else:
    print("It is an unknown operator")
