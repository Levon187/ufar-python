import logging

# reading from a file in other directory
# laura_file = open("../Laura/test.txt", 'r')
# print(laura_file.read())


# appending data to the end of the file
# f = open("log.txt", "a")
# f.write("Hello Nepal!\n")
# f.close()


# using with to work with a file in the body and clodse automaticaly
with open("file.txt", "r") as outfile:
    my_list = outfile.readlines()
    # first_line = outfile.readline()
    # my_list = []
    # for line in range(0,2):
    #     my_list.append(outfile.readline())

# print(my_list)
my_list = [x.strip() for x in my_list]
# print(my_list)


# seek
with open("file.txt", "r") as outfile:
    outfile.seek(20)
    char = outfile.readline()
    print(outfile.tell())

print(char)
