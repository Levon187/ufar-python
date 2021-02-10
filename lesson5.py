'''
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once using only 3-letter words
result -> cat cad cao cag .....
'''


from datetime import datetime

LOGIN = 'VAZGEN'
PASSWORD = 'CHANGEME'
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
# words("catdog")


def words2(letters):
    t1 = datetime.now()
    all_words = []
    letters = set(letters)
    for first_letter in letters:   #this will iterate 6 times
        for second_letter in letters - {first_letter}:  #this will iterate 5 times
            for third_letter in letters - {first_letter, second_letter}:  #this will iterate 4 times
                all_words.append(first_letter + second_letter + third_letter)
    t2 = datetime.now()
    print(t2 - t1)

# words2("catdog")


def is_multiple(n, m):
    return not bool(n % m)
