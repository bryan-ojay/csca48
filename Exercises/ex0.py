def greeting(name):
    '''(str) -> str
    Takes a name in the form of a string, returns a greeting
    with the given name.
    >>> greeting('Bob')
    'Hello Bob how are you today?'
    >>> greeting('Code Mangler')
    'Hello Code Mangler how are you today?'
    '''
    # Create a greeting
    greeting = "Hello " + name + " how are you today?"
    return greeting


def mutate_list(listA):
    '''(list) -> NoneType
    Takes in a list and modifies the elements in the list as follows:
    - Multiplies every integer in the list by 2
    - Inverts every boolean in the list
    - Removes the first and last characters of each string
    - Changes the 0th element of the list to 'Hello'
    >>> listA = [0, 1, 'two', True, 5.0]
    >>> mutate_list(listA)
    >>> listA
    ['Hello', 2, 'w', False, 5.0]
    '''
    # Scan each element in the list starting from index 1
    for i in range(1, len(listA)):

        # Multiply the element by 2 if it is an integer
        if type(listA[i]) == int:
            listA[i] *= 2

        # Invert the element by 2 if it is a boolean
        elif type(listA[i]) == bool:
            listA[i] = not listA[i]

        # Remove the first and last character from the element
        # if it is a string
        if type(listA[i]) == str:
            listA[i] = listA[i][1:-1]

    listA[0] = 'Hello'


def merge_dicts(dictA, dictB):
    '''({str: list of ints}, {str: list of ints}) -> {str: list of ints}
    Takes in two dictionaries where a string value maps to a list of integers,
    returns a new dictionary with all key:value pairs from both dictionaries.
    If the dictionaries share a key, the resulting value will be the list in
    the first dictionary combined with the list in the second dictionary.
    >>> d1 = {'a': [1, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 0], 'd': [10, 11]}
    >>> d3 = merge_dicts(d1, d2)
    >>> d3 == {'a': [1, 3, 2], 'b': [4, 8, 0], 'c': [5, 6, 7], 'd': [10, 11]}
    True
    >>> d4 = merge_dicts(d2, d1)
    >>> d4 == {'a': [2, 1, 3], 'b': [8, 0, 4], 'c': [5, 6, 7], 'd': [10, 11]}
    True
    '''
    # Create new dictionary for the merged values
    dictC = dict()

    for key in dictA:
        # Check for keys in both dictionaries
        if key in dictB:
            dictC[key] = dictA[key] + dictB[key]

        # Check for keys only in dictA
        else:
            dictC[key] = dictA[key]

    for key in dictB:
        # Check for keys only in dictB
        if key not in dictA:
            dictC[key] = dictB[key]

    return dictC
