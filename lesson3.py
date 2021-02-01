def assign_info(name, age):
    '''
    :param name: string
    :param age: int
    :return: is_adult (boolean)
    '''
    print('Hello ' + name + ', your age is ' + str(age))
    # return [name, age, True]
    is_adult = None
    print('Good-bye')
    print(age)
    if age >= 18:
        is_adult = True
    elif age < 7:  # this is a bug TODO creation og age groups
        return 'baby'
    else:
        is_adult = False

    return is_adult


def advertise(is_adult):
    if isinstance(is_adult, bool):
        if is_adult:
            print("come to Aneliq bank")
        else:
            print("say your dad to buy LEGO")
    else:
        print("incorrect data")


name = input("Please enter your first name: ")

try:
    age = int(input("Please enter your age: "))
except:
    age = int(input("Please enter your age in digits: "))

'''  
                                            one time check of numeric input for age
if age.isnumeric():
    age = int(age)
else:
    age = input("this was not a number: ")
    '''


'''  
                                            infinite check of numeric input for age
while not age.isdigit():
    age = input("this was not a number, please enter your age with digits: ")
else:
    age = int(age)
    '''


is_adult = assign_info(name, age)

advertise(is_adult)
