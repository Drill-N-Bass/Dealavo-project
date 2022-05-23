# Różnych cech i wartości dla każdej z nich, może być dowolnie dużo.
# Przykład wyniku wywołania funkcji kartezjan(input):
# [
# {'szerokość': '20cm', 'wysokość': '40cm', 'kolor': 'czarny'},
# {'szerokość': '20cm', 'wysokość': '40cm', 'kolor': 'biały'},
# {'szerokość': '20cm', 'wysokość': '40cm', 'kolor': 'zielony'},
# {'szerokość': '20cm', 'wysokość': '30cm', 'kolor': 'czarny'},
# {'szerokość': '20cm', 'wysokość': '30cm', 'kolor': 'biały'},
# {'szerokość': '20cm', 'wysokość': '30cm', 'kolor': 'zielony'},
# {'szerokość': '16cm', 'wysokość': '40cm', 'kolor': 'czarny'},
# {'szerokość': '16cm', 'wysokość': '40cm', 'kolor': 'biały'},
# {'szerokość': '16cm', 'wysokość': '40cm', 'kolor': 'zielony'},
# {'szerokość': '16cm', 'wysokość': '30cm', 'kolor': 'czarny'},
# {'szerokość': '16cm', 'wysokość': '30cm', 'kolor': 'biały'},
# {'szerokość': '16cm', 'wysokość': '30cm', 'kolor': 'zielony'},
# {'szerokość': '10cm', 'wysokość': '40cm', 'kolor': 'czarny'},
# {'szerokość': '10cm', 'wysokość': '40cm', 'kolor': 'biały'},
# {'szerokość': '10cm', 'wysokość': '40cm', 'kolor': 'zielony'},
# {'szerokość': '10cm', 'wysokość': '30cm', 'kolor': 'czarny'},
# {'szerokość': '10cm', 'wysokość': '30cm', 'kolor': 'biały'},
# {'szerokość': '10cm', 'wysokość': '30cm', 'kolor': 'zielony'},
# ]

import itertools
from itertools import product

input1 = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"}
}

print(list(input1))

import itertools

def dict_product(dicts):
    """
    >>> list(dict_product(dict(number=[1,2], character='ab')))
    [{'character': 'a', 'number': 1},
     {'character': 'a', 'number': 2},
     {'character': 'b', 'number': 1},
     {'character': 'b', 'number': 2}]
    """
    return (dict(zip(dicts.keys(), x)) for x in itertools.product(*dicts.values()))

print(list(dict_product(input1)))
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]


def my_cool_product(**kwargs):

    ar_out = []

    for i in kwargs.items():
        for i1 in kwargs.items():
            final = i, i1
            ar_out.append(final)

print(my_cool_product(arr1 = [1, 2, 3], arr2 = [5, 6, 7])


def dict_product1(dicts):
    return (dict(zip(dicts.keys(), x)) for x in my_cool_product(*dicts.values()))


print(list(dict_product1(input1)))



arr1 = [1, 2, 3]
arr2 = [5, 6, 7]


def my_cool_product(**kwargs):
    print(kwargs.items())
        # for i1 in kwargs[1].items():
        #     final = i, i1
        #     ar_out.append(final)

# my_cool_product(arr1)



def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
##

"""
Tu masz odpowiedź do zadania 1:
"""
input1 = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"}
}

def product_args(*args):
    if args:
        for a in args[0]:
            for prod in product_args(*args[1:]) if args[1:] else ((),):
                yield (a,) + prod

# print(list(product_args("1234", "abce")))
# print(list(product("1234", "abce")))


def dict_product(dicts):
    """
    >>> list(dict_product(dict(number=[1,2], character='ab')))
    [{'character': 'a', 'number': 1},
     {'character': 'a', 'number': 2},
     {'character': 'b', 'number': 1},
     {'character': 'b', 'number': 2}]
    """
    return (dict(zip(dicts.keys(), x)) for x in product_args(*dicts.values()))

print(list(dict_product(input1)))


##
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
arr3 = [8,9,10]


def my_cool_product(*args):
    arr_out = []
    for i in args[0]:
        for i1 in args[1]:
            final = i, i1
            arr_out.append(final)
    return arr_out

print("Test1 :", my_cool_product(arr1, arr2, arr3))

##
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
arr3 = [8,9,10]

def productX(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat # This line will be repeated once
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result
    # for prod in result:
    #     yield tuple(prod)

print("productX(arr1) ", productX(arr1, arr2))
# print("productX(arr1) ", list(productX(arr1, arr2)))

##

"""
Tu masz odpowiedź do zadania 1:
"""
input1 = {
    "szerokość": {"20cm", "16cm", "10cm"},
    "wysokość": {"30cm", "40cm"},
    "kolor": {"czarny", "biały", "zielony"}
}
# https://docs.python.org/3/library/itertools.html#itertools.product
def product_x(*args, repeat=1):
    # product('ABC', 'xy') --> Ax Ay Bx By Cx
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat # This line will be repeated once
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result
    # # if tuple output is needed:
    # for prod in result:
    #     yield tuple(prod)


def dict_product(dicts):

    """
    Function cartesian product for dictionaries.
    Nested function `product_x` is an engine that create all computations necessary.
    `dict_product` is dedicated for dictionary case - as input.


    *dicts return keys
    *dicts.values() return values
    """
    return (dict(zip(dicts.keys(), val)) for val in product_x(*dicts.values()))

print(list(dict_product(input1)))


# print("input astrix * ", *input1.values())