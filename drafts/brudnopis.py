
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

start = timeit.default_timer()
index_finder(b, 1)
stop = timeit.default_timer()

print('Time: index list with `index_finder` func: ', stop - start)


start = timeit.default_timer()

indices = [i for i, x in enumerate(b) if x == 1]
print(indices[0])
stop = timeit.default_timer()

print('Time: index list with comprehension list: ', stop - start)


def loop_index(my_list, item):
    count = 0
    indices = []

    for i in range(0,len(my_list)):
        if item == my_list[i]:
            indices.append(i)

    return indices[0]

start = timeit.default_timer()
print(loop_index(1,b))
stop = timeit.default_timer()

print('Time: index list with loop len: ', stop - start)


def index_of(my_list, item):
    item_e = enumerate(my_list)
    item_f = list(filter(lambda x: x[1] == item, item_e))
    if item_f:
        return item_f[0][0]
    else:
        return -1

start = timeit.default_timer()
index_of(1,b)

stop = timeit.default_timer()

print('Time: index list with lambda: ', stop - start)
print(index_of(1,b))
##
