

#Quention from book
'''age = -1  # an initially invalid choice
while age <= 0:
try:
   age = int(input( Enter your age in years: ))
   if age <= 0:
      print( Your age must be positive )
   except ValueError:
      print( That is an invalid age specification )
   except EOFError:
      print( " was an unexpected error reading input")
      raise'''

# 1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
'''a_list = [n for n in range(50, 87, 10)]
print(a_list)'''

# 1.10What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
'''b_list = [n for n in range (-8, 9,2)]
print(b_list)'''   #List comprehension

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
'''c_list = [2**n for n in range(0, 9)]
print(c_list)'''

#TODO
# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
# a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.


# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
'''from datetime import datetime
# letters.add("r")
# letters.add("c")
# letters |= {"q", "w", "k"}
# letters = letters - {"r"}
def words(letters):
    t1 = datetime.now()
    all_words = []
    letters = set(letters)
    for first_letter in letters:   #this will iterate 6 times
        for second_letter in letters:  #this will iterate 6 times
            if second_letter != first_letter:
                for third_letter in letters:
                    if third_letter != first_letter and third_letter != second_letter:  #  third_letter is not in (first_letter, second_letter)
                        all_words.append(first_letter + second_letter + third_letter)
    t2 = datetime.now()
    print(t2-t1)
# words("catdog")'''

import random
char_set = {'c','a','t','d','o', 'g'}
random.shuffle(char_set)
for i in range(char_set):
 print(''.join(char_set))

