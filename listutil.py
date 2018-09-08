from math import ceil


def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
    sum = 0
    count_unique_list = []

    for x in list:
        if x not in count_unique_list:
            count_unique_list.append(x)

    for x in count_unique_list:
        sum = sum + 1

    return sum


def binary_search(list, element):
    """
    Search the index of the selected element in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    :param list: list of elements to find index elements of
    :param element:
    :return: the index of the selected element in list

    Examples:
    >>> binary_search(['3', '5', '4', '2', '1'], '2')
    1
    >>> binary_search(['3', '5', '4', '2', '1'], '7')
    -1
    >>> binary_search(['k', 'e', 'v', 'i', 'n'], 'v')
    4
    """
    list.sort()

    first_index = 0
    last_index = len(list) - 1

    while first_index <= last_index:
        mid = ceil((last_index + first_index) / 2)
        if element == list[mid]:
            return mid
        elif element == None:
            raise TypeError("Search element must not be none")
        else:
            if element > list[mid]:
                first_index = mid + 1
            elif element < list[mid]:
                last_index = mid - 1
    return -1


