def rsum(listA):
    '''(list of ints) -> int
    Returns the sum of all elements in the given list.
    REQ: len(listA) >= 1
    >>> rsum([1, 2, 3])
    6
    '''
    # Base Case, one element in list
    if len(listA) == 1:
        result = listA[0]

    # Recursive Case, two or more elements in list
    # Divide & Conquer, keep dividing the list until there is one element left
    else:
        result = listA[0] + rsum(listA[1:])

    return result


def rmax(listA):
    '''(list of ints) -> int
    Returns the largest element in the given list.
    REQ: len(list) >= 1
    >>> rmax([1, 5, 10, 8, 6])
    10
    '''
    # Base Cases, one element in list
    if len(listA) == 1:
        result = listA[0]

    # Two or more elements in list, return the bigger element
    elif listA[0] >= listA[1]:
        result = rmax([listA[0]] + listA[2:])

    elif listA[0] < listA[1]:
        result = rmax(listA[1:])

    return result


def second_smallest(listA):
    '''(list of ints) -> int
    Returns the second smallest element in the given list.
    REQ: len(listA) >= 2
    >>> second_smallest([123, 43, 455, 11, 3])
    11
    '''
    # Base Case, two elements in list
    # int(False) is 0, int(True) is 1
    if len(listA) == 2:
        result = listA[int(listA[0] < listA[1])]

    # Recursive Cases, three or more elements in list

    # Compare three values, exclude the biggest of the three from the next
    # recursion, continue until there are two elements

    # First element is biggest
    elif ((listA[1] <= listA[2] <= listA[0]) or
          (listA[2] <= listA[1] <= listA[0])):
        result = second_smallest(listA[1:])

    # Second element is biggest
    elif ((listA[0] <= listA[2] <= listA[1]) or
          (listA[2] <= listA[0] <= listA[1])):
        result = second_smallest([listA[0]] + listA[2:])

    # Third element is biggest
    elif ((listA[0] <= listA[1] <= listA[2]) or
          (listA[1] <= listA[0] <= listA[2])):
        result = second_smallest(listA[0:2] + listA[3:])

    return result


def sum_max_min(listA):
    '''(list of ints) -> int
    Returns the sum of the minimum and maximum elements in the lsit
    REQ: len(listA) >= 1
    >>> sum_max_min([5])
    10
    >>> sum_max_min([122, 34, 3, 12])
    125
    '''
    # Base Case 1: One element in list
    if len(listA) == 1:
        result = 2 * listA[0]

    # Base Case 2: Two elements in list
    elif len(listA) == 2:
        result = listA[0] + listA[1]

    # Recursive Cases: Three or more elements in list

    # Compare three values, exclude the median of the three from the next
    # recursion, continue until there are two elements

    # First element is the median
    elif ((listA[1] <= listA[0] <= listA[2]) or
          (listA[2] <= listA[0] <= listA[1])):
        result = sum_max_min(listA[1:])

    # Second element is the median
    elif ((listA[0] <= listA[1] <= listA[2]) or
          (listA[2] <= listA[1] <= listA[0])):
        result = sum_max_min([listA[0]] + listA[2:])

    # Third element is the median
    elif ((listA[0] <= listA[2] <= listA[1]) or
          (listA[1] <= listA[2] <= listA[0])):
        result = sum_max_min(listA[0:2] + listA[3:])

    return result
