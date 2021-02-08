'''
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2
'''
def by2():
    try:
        num = int(input("Enter an integer positive number: "))
        count = 0
        while num >= 2:
            num /= 2
            count += 1

        print(count)

    except:
        print("ERROR, ENTER AN INTEGER POSITIVE NUMBER")


'''
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device
'''


def calc():
    n1 = int(input("Enter the first number: "))
    print(n1)

    op = input("Enter the operation: ")
    print(op)

    n2 = int(input("Enter the second number: "))
    print(n2)

    if op == '+':
        ans = n1 + n2
    elif op == '-':
        ans = n1 - n2
    elif op == '/':
        ans = n1 / n2
    else:
        ans = n1 * n2

    print(str(n1) + " " + str(op) + " " + str(n2) + " = " + str(ans))

# calc()
# by2()
