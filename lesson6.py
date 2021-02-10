from lesson5 import is_multiple
from time import time
from moviepy.editor import *        # pip install moviepy
from bottle import route, run, template    # pip install bottle



def book_example():
    age = -1  # an initially invalid choice
    while age <= 0:
        try:
            age = input("Enter your age in years:")
            if age <= 0:
                print( "Your age must be positive" )
        except ValueError:
            print( "Invalid response" )
        except TypeError:
            print( "There was an unexpected error reading input." )
            raise


# n = int(input("first number: "))
# m = int(input("second number: "))
# print(is_multiple(n, m))


@route('/hello')
def hello():
    return "Hello World!"

@route('/goodbye')
def goodbye():
    return "Goodbye Mask!"

run(host='localhost', port=8080, debug=True)
