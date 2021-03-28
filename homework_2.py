#Use decorator to estimate pi to n number of decimal places
import math
def get_pi_n(func):
    def inner(n):
        print("Pi estimated to n number of decimal places: ")
        return func(n)
    return inner
@get_pi_n
def get_pi(n):
    pi = round(math.pi,n)
    return pi
print(get_pi(3))

#Use lambda to split a given data list into several small sections
import numpy as np
split_list = lambda list1, sections: [list(i) for i in (np.array_split(list1,sections))]
print(split_list([1,2,3,4,"5","6","7","8"],4))

#Use lambda to perform some simple statistics on a list of values
list_stats = lambda list1: {
                           "mean" : np.mean(list1),
                            "min" : np.min(list1),
                            "max" : np.max(list1)
                           }
print(list_stats([1,2,3,4,5,6,7,8,9]))

