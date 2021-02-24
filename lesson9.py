def ad_show_by_age_group(user_age):
    if 10 < user_age <= 16:
        print('Kinder Surprise')
    if 16 < user_age <= 21:
        print('Coca-Cola')
    if 21 < user_age <= 27:
        print('Corona beer')


# //////////////////////     filter
def lower_zero(x):
    if x < 0:
        return x


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
less_than_zero_version2 = list(filter(lower_zero, number_list))

# print(less_than_zero)
# print(less_than_zero_version2)

# ////////////////////// reduce
product = 1
my_list = [1, 2, 3, 4]
for num in my_list:
    product = product * num


# def multiply(x, y):
#     return x*y

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# product2 = reduce(multiply, [1, 2, 3, 4])

# print(product)
# print(product2)


# /////////////////////////////    zip

first_names = ["Levon", "Robert", "Serj", "Nikol", "Upcoming..."]
last_names = ["Ter-Petrosyan", "Kocharyan", "Sargsyan", "Pashinyan"]
years_of_government = ["1991-1998", "1998-2008", "2008-2018"]

# [("Levon", "Ter-Petrosyan", "1991-1998"), (......), (.....), ....]

result = []

for i in range(len(years_of_government)):
    # result[i] = first_names[i] + last_names[i] + years_of_government[i]     this is incorrect
    result.append((first_names[i], last_names[i], years_of_government[i]))

print(result)

#  discussion of adding key, value pair in dict
president = {'fist_name': 'Levon', 'last_name': 'Ter_petrosyan', 'years_of_government': '1991-1998'}
president['nick_name'] = 'blind'
# print(president)


# ///////////////    finally using ZIP

result_using_zip = zip(first_names, last_names, years_of_government)  # it creates an iterator
result_using_zip = list(zip(first_names, last_names, years_of_government))  # we will use list() to get the full picture
print(result_using_zip)

from itertools import zip_longest
result_using_zip_longest = list(zip_longest(first_names, last_names, years_of_government, fillvalue=' go vote for it'))
print(result_using_zip_longest)


# ////////////   default argument in python

def fill_up_form(first_name, last_name, phone_number, company, address, citizenship="Armenia"):
    letter = f'Hi my name is {first_name} {last_name}, I want to subscribe to your service {company}!!!.' \
             f'\nMy number is {phone_number} and my address is {address}. Citizen of {citizenship}.' \
             f'\nSincerely yours :)'
    return letter


print(fill_up_form('Vazgen',
                   'Manukyan',
                   company='KRISP',
                   phone_number='+374555555555',
                   address='Fuchik 54/2',
                   citizenship="Sudan"))



#  CODEWARS.COM   ????     try to solve in recusive way


def solution(string):
    new_string = ''
    for i in range(len(string)-1, -1, -1):
        new_string = new_string + string[i]
    return new_string


def solution(string):
    new_string = ''
    for letter in string:
        new_string = letter + new_string
    return new_string
