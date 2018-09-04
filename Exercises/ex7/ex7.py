def rsum(objA):
    '''(int, list of int or list of list) -> int
    Returns the given integer, or returns the sum of all integers in the list
    if a list is given.
    >>> rsum([1, [2, 3]])
    6
    >>> rsum([12, [[34, 56], [34]]])
    136
    >>> rsum([])
    0
    '''
    # Set the starting sum to 0
    result = 0

    # Base Cases: object is an integer, or object is a list with no elements
    if isinstance(objA, int):
        result = objA

    elif len(objA) == 0:
        result = 0

    # Recursive Case: object is a list
    # Add up the elements in the list
    elif len(objA) > 0:
        result = rsum(objA[0]) + rsum(objA[1:])

    return result


def rmax(objA):
    '''(list of int or list of list) -> int
    Returns largest integer in the given list.
    REQ: len(objA) >= 1 if objA is a list
    >>> rmax([1, [2, 3]])
    3
    >>> rmax([12, [[34, 56], [34]]])
    56
    '''
    result = rmax_helper(objA)
    return result[0]


def rmax_helper(objA):
    '''(list of int or list of list) -> list of int
    Returns a list containing the largest integer in the given list.
    REQ: len(objA) >= 1 if objA is a list
    >>> rmax_helper([1, [2, 3]])
    [3]
    >>> rmax_helper([12, [[34, 56], [34]]])
    [56]
    '''
    # Base Case: object is an integer
    if len(objA) == 0:
        result = objA

    # Recursive Cases
    # obj is a list containing one integer
    elif len(objA) == 1 and isinstance(objA[0], int):
        result = objA

    # obj is a list containing a nested list
    elif len(objA) == 1 and isinstance(objA[0], list):
        result = rmax_helper(objA[0])

    # obj is a list with 2 or more elements
    # Exclude the smaller item in the next function call
    elif len(objA) >= 2:
        if rmax_helper(objA[0:1]) <= rmax_helper(objA[1:2]):
            result = rmax_helper(objA[1:])

        else:
            result = rmax_helper(objA[0:1] + objA[2:])

    return result


def second_smallest(objA, depth=0):
    '''(list of int or list of list) -> int or list of int
    Returns the integer if an integer is given, and returns the second smallest
    element if a list if a list is given.
    REQ: len(objA) == 2 if objA is a list
    >>> second_smallest([1, [2, 3]])
    2
    >>> second_smallest([12, [[34, 56], [34]]])
    34
    '''
    # Base Cases, obj is an empty list or a list with an integer element
    if len(objA) == 0:
        result = objA

    elif len(objA) == 1 and isinstance(objA[0], int):
        result = objA

    # Recursive Case, obj is a nested list or a list with multiple elements

    # Nested list with length 1: call the function on the element
    elif len(objA) == 1 and isinstance(objA[0], list):
        result = second_smallest(objA[0], depth+1)

    # List with length 2: call the function on the list version of both
    # elements
    elif len(objA) == 2:
        result = (second_smallest(objA[0:1], depth+1) +
                  second_smallest(objA[1:], depth+1))

    # List with length 3
    # Call the function on the list version of the first 3 elements
    elif len(objA) >= 3:
        min1 = second_smallest(objA[0:1], depth+1)
        min2 = second_smallest(objA[1:2], depth+1)
        min3 = second_smallest(objA[2:], depth+1)
        values = min1 + min2 + min3

        # If the length of the list decreases to less than 3 due to adding
        # empty lists, call the function again
        if len(values) < 3:
            result = second_smallest(values, depth+1)

        # Else, call the function on the values again without the biggest
        # element
        elif ((values[1] <= values[2] <= values[0]) or
              (values[2] <= values[1] <= values[0])):
            result = second_smallest(values[1:], depth+1)

        elif ((values[0] <= values[2] <= values[1]) or
              (values[2] <= values[0] <= values[1])):
            result = second_smallest(values[0:1] + values[2:], depth+1)

        elif ((values[0] <= values[1] <= values[2]) or
              (values[1] <= values[0] <= values[2])):
            result = second_smallest(values[0:2] + values[3:], depth+1)

    # Once the function has reached the final depth again, check if there are
    # 2 numbers in the result list
    # If not, call the function again
    if depth == 0:
        if len(result) == 2:
            result = result[int(result[0] < result[1])]

        else:
            result = second_smallest(result)

    return result


def sum_max_min(objA, depth=0):
    '''(list of int or list of list) -> int or list of int
    Returns the integer if an integer is given, and returns the second smallest
    element if a list if a list is given.
    REQ: len(objA) == 2 if objA is a list
    >>> sum_max_min([1, [2, 3]])
    4
    >>> sum_max_min([12, [[34, 56], [34]]])
    68
    '''
    # Base Cases, obj is an empty list or a list with an integer element
    if len(objA) == 0:
        result = objA

    elif len(objA) == 1 and isinstance(objA[0], int):
        result = objA

    # Recursive Case, obj is a nested list or a list with multiple elements

    # Nested list with length 1: call the function on the element
    elif len(objA) == 1 and isinstance(objA[0], list):
        result = sum_max_min(objA[0], depth+1)

    # List with length 2: call the function on the list version of both
    # elements
    elif len(objA) == 2:
        result = (sum_max_min(objA[0:1], depth+1) +
                  sum_max_min(objA[1:], depth+1))

    # List with length 3
    # Call the function on the list version of the first 3 elements
    elif len(objA) >= 3:
        med1 = sum_max_min(objA[0:1], depth+1)
        med2 = sum_max_min(objA[1:2], depth+1)
        med3 = sum_max_min(objA[2:], depth+1)
        values = med1 + med2 + med3

        # If the length of the list decreases to less than 3 due to adding
        # empty lists, call the function again
        if len(values) < 3:
            result = sum_max_min(values, depth+1)

        # Else, call the function on the values again without the median
        # element
        elif ((values[1] <= values[0] <= values[2]) or
              (values[2] <= values[0] <= values[1])):
            result = sum_max_min(values[1:], depth+1)

        elif ((values[0] <= values[1] <= values[2]) or
              (values[2] <= values[1] <= values[0])):
            result = sum_max_min(values[0:1] + values[2:], depth+1)

        elif ((values[0] <= values[2] <= values[1]) or
              (values[1] <= values[2] <= values[0])):
            result = sum_max_min(values[0:2] + values[3:], depth+1)

    # Once the function has reached the final depth again, check if there are
    # 1 or 2 numbers in the result list
    # If not, call the function again
    if depth == 0:
        if len(result) == 1:
            result = 2 * result[0]

        elif len(result) == 2:
            result = result[0] + result[1]

        else:
            result = sum_max_min(result)

    return result


if __name__ == "__main__":
    print(rmax([5, [], [12, 8, [-2]]]))