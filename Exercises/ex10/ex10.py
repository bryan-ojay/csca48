def radix_sort(listA):
    '''(list of int) -> list of int
    Takes in a list of integers, returns the sorted version of the list.
    REQ: int in listA >= 0
    >>> radix_sort([2198, 23, 234, 0])
    [0, 23, 234, 2198]
    '''
    return _radix_helper(listA, 1)


def _radix_helper(listA, place):
    '''(list of int, int) -> list of int
    Takes in a list of integers and the place value to sort it at. Returns
    the sorted version of the list of integers.
    REQ: all int in listA >= 0
    REQ: place >= 1
    REQ: place % 10 == 0 for all place > 1
    >>> _radix_helper([2198, 23, 234, 0], 1)
    [0, 23, 234, 2198]
    '''
    # Create list containing 10 slots
    # Create new list to insert items from listA
    # Assign variable for number of integers higher than the next place value
    slot_list = ([], [], [], [], [], [], [], [], [], [])
    sort_list = []
    next_place = 0

    # Loop through the list
    i = 0
    while i < len(listA):

        # Check if the number is bigger than the next place value
        if listA[i] >= (place * 10):
            next_place += 1

        # Move the integer into the corresponding slot
        slot_num = (listA[i] // place) % 10
        slot_list[slot_num].append(listA[i])

        i += 1

    # Loop through the slot list after all of the elements have been removed
    for slot in slot_list:
        while len(slot) > 0:
            # Move the integers from each slot back into the lsit
            sort_list.append(slot.pop(0))

    # Base Case, all the numbers are less than the next place value
    if next_place == 0:
        sorted_list = sort_list

    # Recursive Case, there are still numbers higher than the next highest
    # place value
    else:
        sorted_list = _radix_helper(sort_list, place * 10)

    return sorted_list
