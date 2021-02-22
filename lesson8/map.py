temps = [('Yerevan', 2), ('Vanadzor', -3), ('Abovyan', 5)]  # [('Yerevan', F)......]

temps2 = [{'Yerevan': 2, 'Vanadzor': -3, 'Abovyan': 5}]


# for c, t in temps2[0].items():
#     print(c, t)

# (0°C × 9/5) + 32 = 32°F


def from_c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp


f_temps = []

# for t in temps:
#     city = t[0]
#     c_temp = t[1]
#     print(city)
#     f_temp = from_c_to_f(t[1])
#     my_tuple = (city, f_temp)
#     f_temps.append(my_tuple)

for i in temps:
    f_temps.append((i[0], from_c_to_f(i[1])))

print(f_temps)


def c_to_f(elem):
    city = elem[0]
    f_temp = elem[1] * 9 / 5 + 32
    return city, f_temp


f_temps2 = map(c_to_f, temps)
print(list(f_temps2))

# ///////////////////////////////////////

def power(n):
    return n ** 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_numbers = list(map(power, numbers))

print(new_numbers)