# Write a short recursive Python function that finds the minimum and maximum
# values in a sequence without using any loops.
list_1 = [22, 4, 5, 54, 7, 9, 6,22,5,8]
n = len(list_1)


def max_function(list_1, n):
    if n == 1:
        return list_1[0]
    else:
        return max(list_1[n - 1], max_function(list_1, n - 1))


def min_function(list_1, n):
    if n == 1:
        return list_1[0]
    else:
        return min(list_1[n - 1], max_function(list_1, n - 1))


print("The maximum elem is:" + str(max_function(list_1, n)))
print("The minimum elem is:" + str(min_function(list_1, n)))