import random
import timeit
import pandas as pd

"""
I will define a seed for random. 
With this approach 
I can test the time of execution with the seam result each time, 
because the list will have the same content every time.
"""
random.seed(2)

"""
I will create a few lists with 

list_a -> 100 numbers selected from the range 0 to 100 without duplicates.
list_b -> 1,000 numbers selected from the range 0 to 1,000 without duplicates.
list_c -> 10,000 numbers selected from the range 0 to 10,000 without duplicates.
list_d -> 100,000 numbers selected from the range 0 to 100,000 without duplicates.
list_e -> 1,000,000 numbers selected from the range 0 to 1,000,000 without duplicates.
list_f -> 10,000,000 numbers selected from the range 0 to 10,000,000 without duplicates.
list_g -> 100,000,000 numbers selected from the range 0 to 100,000,000 without duplicates.
"""
list_a = random.sample(range(101), 100)
list_b = random.sample(range(1001), 1000)
list_c = random.sample(range(10001), 10000)
list_d = random.sample(range(100001), 100000)
list_e = random.sample(range(1000001), 1000000)
# list_f = random.sample(range(10000001), 10000000)
# list_g = random.sample(range(100000001), 100000000)
# list_h = random.sample(range(1000000001), 1000000000)


list_all_index_method_time = []
final_data_output = {}

start = timeit.default_timer()
l_ind_a = list_a.index(1)
stop = timeit.default_timer()
# print('Time: index list with `index`: ', stop - start)
list_a_index_method_time = stop - start
list_all_index_method_time.append(list_a_index_method_time)

start = timeit.default_timer()
l_ind_b = list_b.index(1)
stop = timeit.default_timer()
# print('Time: index list with `index`: ', stop - start)
list_b_index_method_time = stop - start
list_all_index_method_time.append(list_b_index_method_time)

start = timeit.default_timer()
l_ind_c = list_c.index(1)
stop = timeit.default_timer()
# print('Time: index list with `index`: ', stop - start)
list_c_index_method_time = stop - start
list_all_index_method_time.append(list_c_index_method_time)

start = timeit.default_timer()
l_ind_d = list_d.index(1)
stop = timeit.default_timer()
# print('Time: index list with `index`: ', stop - start)
list_d_index_method_time = stop - start
list_all_index_method_time.append(list_d_index_method_time)

start = timeit.default_timer()
l_ind_e = list_e.index(1)
stop = timeit.default_timer()
# print('Time: index list with `index`: ', stop - start)
list_e_index_method_time = stop - start
list_all_index_method_time.append(list_e_index_method_time)

# start = timeit.default_timer()
# l_ind_f = list_f.index(1)
# stop = timeit.default_timer()
# # print('Time: index list with `index`: ', stop - start)
# list_f_index_method_time = stop - start
# list_all_index_method_time.append(list_f_index_method_time)

final_data_output["index_method"] = list_all_index_method_time

all_random_lists = [list_a, list_b, list_c, list_d, list_e]

# # Sorted lists:
# for i_list in all_random_lists:
#     i_list = i_list.sort()

# print(list_a) # Test


list_all_find_func_time = []
list_all_find_index_finder_func_time = []
list_all_find_comprehension_list_time = []
list_all_find_list_with_loop_len_time = []
list_all_find_list_with_lambda_time = []
list_all_find_list_fastest_method_time = []

"""
List of method that will be tested:
"""


def find(my_list, item):
    if item not in my_list:
        print(None)
    for i in range(len(my_list)):
        if my_list[i] == item:
            yield i


def index_finder(my_list, item):
    """A generator function, if you might not need all the indices"""
    start = 0

    while True:
        try:
            start = my_list.index(item, start)
            yield start
            start += 1
        except ValueError:
            break
        except IndexError:
            return None


def index_of(my_list, item):
    item_e = enumerate(my_list)
    item_f = list(filter(lambda x: x[1] == item, item_e))
    if item not in my_list:
        return None
    elif item_f:
        return item_f[0][0]
    else:
        return -1


def enumerate_index(my_list, item):
    if item not in my_list:
        return None

    indices = [i for i, x in enumerate(my_list) if x == item]
    return indices[0]


def loop_index(my_list, item):
    count = 0
    indices = []

    if item not in my_list:
        return None

    for i in range(0, len(my_list)):
        if item == my_list[i]:
            indices.append(i)

    return indices[0]


def index_of(my_list, item):
    item_e = enumerate(my_list)
    item_f = list(filter(lambda x: x[1] == item, item_e))

    if item_f:
        return item_f[0][0]
    else:
        return -1


def fastest_index_method(my_list, item):
    """
    returns index of x in ordered list.
    If x is between two items in the list, the index of the lower one is returned.
    """

    l = len(my_list)  # 5
    i = l // 2  # 2
    j = i // 2  # 1

    while (j > 0):
        if item < my_list[i]:
            i -= j
        else:
            i += j
        j = j // 2

    if item not in my_list:
        return None

    return i


for name in all_random_lists:
    # loop related to `find()` method:
    start = timeit.default_timer()
    l_ind_find = list(find(name, 1))[0]
    stop = timeit.default_timer()
    # print('Time: index list with `find()` func: ', stop - start) # test
    list_find_func_method_time = stop - start
    list_all_find_func_time.append(list_find_func_method_time)

    # loop related to `index_finder()`method:
    start = timeit.default_timer()
    l_ind_i_find = list(index_finder(name, 1))[0]
    stop = timeit.default_timer()
    # print('Time: index list with `find()` func: ', stop - start) # test
    list_find_index_finder_func_time = stop - start
    list_all_find_index_finder_func_time.append(list_find_index_finder_func_time)

    # loop related to comprehension list method:
    start = timeit.default_timer()
    l_ind_enum = enumerate_index(name, 1)
    stop = timeit.default_timer()
    list_find_comprehension_list_time = stop - start
    list_all_find_comprehension_list_time.append(list_find_comprehension_list_time)

    # loop related to loop len method:
    start = timeit.default_timer()
    l_ind_loop_idx = loop_index(name, 1)
    stop = timeit.default_timer()
    list_find_list_with_loop_len_time = stop - start
    list_all_find_list_with_loop_len_time.append(list_find_list_with_loop_len_time)

    # loop related to index list with lambda method:
    start = timeit.default_timer()
    l_ind_mabda = index_of(name, 1)
    stop = timeit.default_timer()
    list_find_list_with_lambda_time = stop - start
    list_all_find_list_with_lambda_time.append(list_find_list_with_lambda_time)

    # loop related to the fastest method:
    start = timeit.default_timer()
    l_ind_fastest = fastest_index_method(name, 1)
    stop = timeit.default_timer()
    list_find_list_with_fastest_method_time = stop - start
    list_all_find_list_fastest_method_time.append(list_find_list_with_fastest_method_time)

final_data_output["find func method"] = list_all_find_func_time
final_data_output["find index finder"] = list_all_find_index_finder_func_time
final_data_output["find comprehension list"] = list_all_find_comprehension_list_time
final_data_output["find list with loop_len"] = list_all_find_list_with_loop_len_time
final_data_output["find list with lambda"] = list_all_find_list_with_lambda_time
final_data_output["find list with fastest method"] = list_all_find_list_fastest_method_time

df = pd.DataFrame(final_data_output)

"""Print an entire pandas DataFrame in Python:"""
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)

# pd.DataFrame.plot(df)

