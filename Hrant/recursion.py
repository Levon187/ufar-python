# 4.19

def maxInSeq(seq):
    if len(seq) == 1:
        return seq[0]
    maxElem = seq[0]
    del seq[0]
    return max(maxElem, maxInSeq(seq))


def minInSeq(seq):
    if len(seq) == 1:
        return seq[0]
    minElem = seq[0]
    del seq[0]
    return min(minElem, minInSeq(seq))


# 4.12

def product(m, n):
    if n > m:
        t = m
        m = n
        n = t

    if n == 1:
        return m
    return product(m, n - 1) + m


# 4.13

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks


def draw_ruler(number_inches, major_length):
    draw_line(major_length, '0')  # 0 inch line
    for j in range(1, 1 + number_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


draw_ruler(2, 4)
print(product(8, 10001))
print(maxInSeq([1000, 2, 3, 4, 5, 6]))
print(minInSeq([1000, 2, 3, 4, 5, 6]))
