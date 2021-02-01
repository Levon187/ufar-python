#tranlsator
# Narek -> Nzrzk
# Karen -> Kzrzn
# Ararat -> Zrzrzt

def translate(phrase):
    new_phrase = ''
    vowels = "aeuio"
    for char in phrase:
        if char in vowels:
            new_phrase = new_phrase + 'z'
        elif char in vowels.upper():
            new_phrase = new_phrase + 'Z'
        else:
            new_phrase = new_phrase + char
    # print(new_phrase)


translate("I want to have a rest in Miami!")

#number
number_grids = [
    [['A', 'B'], 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grids[0][0][1])
