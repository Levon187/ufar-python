#   list comprehension
#example 1
start_point = [1, -5, 8]
# next_point = []
# for cord in start_point:
#     if cord < 0:
#         next_point.append(cord)
#     else:
#         next_point.append(cord*2)

next_point =[cord*2 if cord > 0 else cord for cord in start_point]
# print(next_point)


#example 2
movies = [('Matrix', 1999), ('Inception', 2010), ('Batman: Forever', 1995), ('Die Hard', 1988)]
# old_movies = []
# for movie_name, movie_year in movies:  # for movie in movies:   movie_name, movie_year = movie
#     if movie_year < 2000:
#         old_movies.append(movie_name)# old_movies = old_movies + movie_name

old_movies = [movie_name for movie_name, year in movies if year < 2000]

# print(old_movies)



#example 3
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
b = [1,2,3,4,5,6,7,8]


# result = []
# for x in a:
#     for y in b:
#         result.append((x,y))

result = [(x,y) for x in a for y in b]

print(len(result), result)

# excersice
# please write a code with for loop and list comprehension
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
b = [1,2,3,4,5,6,7,8]                    #  result = [("A",1), ("B", 2), .......]



#  try/except
# TypeError:    input string and try to divide a integer with a string type
# ZeroDivisionError:    dividing by zero
# ValueError:          int() function expect to get digit characters to convert it to an integer
def hundred_divide_by_input():
    try:
        num = int(input("please enter the number: "))
    except ValueError as error:
        print("invalid input, not numerical", error)
        hundred_divide_by_input()
        return
    result = None
    try:
        result = 100/num
    except ZeroDivisionError:
        result = 'infinite'
    except Exception as error:
        print(error, type(error))
    print(result)

# hundred_divide_by_input()