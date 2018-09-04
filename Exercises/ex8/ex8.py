def edit_distance(s1, s2):
    '''(str, str) -> int
    Returns the minimum number of single character changes that would require
    turning s1 to s2.
    >>> edit_distance('abc', 'aaa')
    2
    >>> edit_distance('cadawedww', '123456789')
    9
    '''
    # Base Case, one of the strings has a length of 0
    if len(s1) == 0 or len(s2) == 0:
        result = 0

    # Recursive Case, current characters are the same
    elif s1[0] == s2[0]:
        result = edit_distance(s1[1:], s2[1:])

    # Recursive Case, current characters are different
    elif s1[0] != s2[0]:
        result = 1 + edit_distance(s1[1:], s2[1:])

    return result

def subsequence(s1, s2):
    '''(str, str) -> bool
    Returns True iff removing letters in s2 can yield s1
    REQ: len(s2) >= len(s1)
    >>> subsequence('dog', 'XYZdABCo123g!!!')
    True
    >>> subsequence('cat', 'ctaaaaa')
    False
    '''
    # Base Case, s1 is of length 0
    if len(s1) == 0:
        result = True

    # Base Case, s2 is smaller than s1
    elif len(s2) < len(s1):
        result = False

    # Recursive Case
    elif s1[0] == s2[0]:
        result = subsequence(s1[1:], s2[1:])

    elif s1[0] != s2[0]:
        result = subsequence(s1, s2[1:])

    return result

def perms(s):
    '''(str) -> set of str
    Returns a set of all possible permutations of the string s.
    >>> perms('123') == {'123', '132', '213', '231', '312', '321'}
    True
    '''
    # Create empty set
    perm = set()

    # Base Case, string is 1 or less characters (1 permutation)
    if len(s) <= 1:
        perm = {s}

    # Base Case, string has 2 characters (2 permutations)
    elif len(s) == 2:
        perm = perm.union({s[0] + s[1], s[1] + s[0]})

    # Recursive Case, string has more than 2 characters (up to n! permutations)
    elif len(s) > 2:
        # Create sub=permutations for all characters in s except the first one
        sub_perm = perms(s[1:])
        # Loop through every element in the sub-permutation
        for element in sub_perm:
            # Add the first character to every index of every sub-perm element
            for i in range(len(element)+1):
                # Add the new element to the set
                perm.add(element[:i] + s[0] + element[i:])

    return perm
