from container import *


def banana_verify(source, goal, cont, moves):
    '''(str, str, Container, list of str) -> bool
    Takes in a source and goal word, a container to store items, and a list of
    moves to permutate the source word into the goal word. Returns True if the
    given moves properly permutate the source word into the goal word.
    Returns False if the game is played improperly.
    REQ: len(source) >= 1
    REQ: len(goal) >= 1
    >>> banana_verify('BALL', 'LLAB', Stack(),
    ... ['P', 'P', 'P', 'M', 'G', 'G', 'G'])
    True
    >>> banana_verify('BALL', 'LLAB', Queue(),
    ... ['P', 'P', 'P', 'M', 'G', 'G', 'G'])
    False
    '''
    # Create empty string to move letters
    # Create a boolean to validate if the game doesn't crash
    result = ""
    no_errors = True

    # Run through all of the moves
    i = 0
    while i < len(moves) and no_errors:
        # Put function
        if (moves[i] == 'P'):
            # Insert the first letter in source into container
            # Remove the letter from source
            try:
                cont.put(source[0])
                source = source[1:]
            except:
                no_errors = False

        # Move function
        elif (moves[i] == 'M'):
            # Add the first letter in source into the result
            # Remove the letter from source
            try:
                result += source[0]
                source = source[1:]
            except:
                no_errors = False

        # Get function
        elif (moves[i] == 'G'):
            # Add the first element from the container to the result
            try:
                result += (cont.get())
            except:
                no_errors = False

        # Improper input
        else:
            no_errors = False

        i += 1

    # Check if the result and goal word match, the container is empty,
    # and the game was played properly
    valid_moves = (result == goal) and (cont.is_empty())
    return (valid_moves and no_errors)

if __name__ == "__main__":
    # Testing Container class
    print(banana_verify("AB", "AB", Stack(), ["M", "M"]))
    print(banana_verify("AB", "BA", Stack(), ["P", "M", "G"]))
    print(banana_verify("AB", "BA", Queue(), ["P", "M", "G"]))
    print(banana_verify("AB", "BA", Bucket(), ["P", "M", "G"]))
    # Testing for result of error, should output False
    print(banana_verify("AB", "BA", Bucket(), ["P", "P"]))

    # Exercise 1 Tests
    src_word = "BANANA"
    # 2.
    print(banana_verify(src_word, "AAANNB", Stack(), ["P", "M", "P", "M", "P", "M", "G", "G", "G"]))
    # 3.
    print(banana_verify(src_word, "BNAAAN", Bucket(), ["M", "P", "M", "M", "G", "P", "M", "G"]))
    print(banana_verify(src_word, "BNAAAN", Stack(), ["M", "P", "M", "M", "G", "P", "M", "G"]))
    print(banana_verify(src_word, "BNAAAN", Queue(), ["M", "P", "M", "M", "G", "P", "M", "G"]))