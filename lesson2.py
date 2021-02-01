# list adding and removing parameters

names_list = ["Ashot", "Vazgen", "Anna", "Vazgen"]
# names_list.append("Vagharsh")
# names_list.insert(1, "Amalya")
# names_list.pop()
#
# for i in names_list:
#     if i == "Vazgen":
#         names_list.remove(i)
#
# for i in range(0, len(names_list)):
#     if names_list[i] == "Vazgen":
#         names_list.remove(names_list[i])
#
# count = names_list.count("Vazgen")
# for i in range(0, count):
#     names_list.remove("Vazgen")
# index = 0
# for i in names_list:
#     print(index, i)
#     index += 1

for k, v in enumerate(names_list, start=1):
    print(k, v)

# names_list.remove("Vazgen")

# print(names_list)


#     list: slices, reverse and sort

# my_list = ["A", "B", "c", "+", "D", "E"]
# my_list[1] = "Z"
# print(my_list)

# print(my_list[0:3])
# print(my_list[1:4])
# print(my_list[10])   list index out of range
# print(my_list[-1])
# print(my_list[-3:-1])
# my_list.reverse()
# print(my_list)
# sort_list = sorted(my_list)
# print(sort_list)
# print(my_list)

#  string
'''
my_string = "I am going to Miami this summer.?!"
print(my_string)
print(my_string[0])
print(my_string[1:3])
print(my_string[-2])
print(my_string.count("Z")) # counts how many mentioned symbols in the string
print(my_string.strip()) # cuts spaces from start and end if no parameter given
my_string = my_string.replace(".", "").replace("?", "").replace("!", "")
print(my_string)
print(my_string.split())
print(my_string.find('m'))
print(my_string.upper())
print(my_string.startswith("I am"))
names_list = ["Ashot", "Vazgen", "Anna", "Artur"]
new_string = ':'.join(names_list)
print(new_string)
'''

#  tuple
'''
my_list = [5, 6]
my_list[0] = 10
print(my_list, end='\t')
my_tuple = (5, 6)
print(my_tuple[0])
x, y = my_tuple
print("this is our coordinates: ", x, y)
'''

# dict
'''
my_dict = {'Jan': 'January', 'Feb': 'Feburary', 'Dec': 'December'}
# print(my_dict['Jan'])
# print(my_dict.get('Aug', 'hey guys, none such month yet'))
my_dict['Mar'] = "March"

for i in my_dict:    # === for i in my_dict.keys():
    print(i, my_dict[i])

my_dict.values()
my_dict.keys()
my_dict.items()

# for k, v in my_dict.items():
#     print(k, v)

poped_month = my_dict.pop('Mar')  # it saves the value
print(my_dict)
print(poped_month)
new_dict = my_dict.copy()
print(new_dict)

'''