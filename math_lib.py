import numpy as np

def min(lst):
    min_so_far = np.inf
    for i in lst:
        if i < min_so_far:
            min_so_far = i
    return min_so_far


def max(lst):
    max_so_far = -np.inf
    for i in lst:
        if i > max_so_far:
            max_so_far = i
    return max_so_far


def mean(lst):
    sum = 0
    len = 0
    for i in lst:
        sum += i
        len += 1
    return sum/len

def median(lst):
    pass


def variance(lst):
    pass


def std(lst):
    pass


list1 = [3, 56, 8, 2, 90]
print(min(list1))
print(max(list1))
print(mean(list1))
print(median(list1))
print(variance(list1))
print(std(list1))
