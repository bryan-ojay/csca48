"""
# Copyright Nick Cheng, 2016, 2018
# Copyright Bryan Oladeji, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.

# Create a global tuple containing all the valid variables
# Create a global dictionary to hold the winning values for Players A and E
VARIABLES = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
SYMBOLS = ('+', '*', '-', '(', ')')
WIN_VALUE = {'A': 0, 'E': 1}


def build_tree(formula):
    '''(str) -> FormulaTree
    Takes in a string representation of a boolean formula, returns the
    corresponding FormulaTree representation of the formula, given that it is
    valid. If the formula is not valid, None is returned.
    Valid formulas are of one of the following types:
    F1
    (F1 * F2)
    (F1 + F2)
    - F1
    where F1 and F2 are also valid boolean formulas.
    REQ: all characters in formula are in VARIABLES and SYMBOLS
    >>> build_tree("x-y") is None
    True
    >>> build_tree("(-x+y)")
    OrTree(NotTree(Leaf('x')), Leaf('y'))
    >>> build_tree("((x*y)+z)")
    OrTree(AndTree(Leaf('x'), Leaf('y')), Leaf('z'))
    '''
    # Defaulted the variable for the FormulaTree to an invalid input
    tree = None

    # Base Case, formula is empty: invalidate the formula
    if not formula:
        tree = None

    # Base Case, formula is a boolean variable
    elif formula in VARIABLES:
        tree = Leaf(formula)

    # Recursive Case 1: Formula is a negation of a boolean formula (NotTree)
    # Set that formula's children to be everything after the symbol
    elif formula[0] == '-':
        tree = NotTree(build_tree(formula[1:]))

    # Recursive Case 2: Formula is a boolean formula
    elif formula[0] == '(' and formula[-1] == ')':
        # Loop through the formula string
        ind = 1

        while ind < len(formula) - 1:
            # Check if formula contains nested boolean formulas
            if formula[ind] == '(':
                brackets = 1
                ind += 1

                while brackets != 0 and ind < len(formula) - 1:
                    # For each open bracket, add a new level of nesting
                    if formula[ind] == '(':
                        brackets += 1

                    # For each closing bracket, remove a level of nesting
                    elif formula[ind] == ')':
                        brackets -= 1

                    # Invalidate the tree if an invalid character is found
                    elif not (formula[ind] in VARIABLES or
                              formula[ind] in SYMBOLS):
                        tree = None
                        ind = len(formula) - 2

                    ind += 1

            # Check if formula is an AndTree/OrTree formula
            # Set the formula's children to be everything before the symbol,
            # and everything after the symbol, then stop the while loop
            if formula[ind] == '*':
                tree = AndTree(build_tree(formula[1:ind]),
                               build_tree(formula[ind+1:-1]))
                ind = len(formula) - 1

            elif formula[ind] == '+':
                tree = OrTree(build_tree(formula[1:ind]),
                              build_tree(formula[ind+1:-1]))
                ind = len(formula) - 1

            ind += 1

    # Check if there is an invalid formula nested in the boolean formula
    # The whole tree is then made invalid
    if 'None' in str(tree):
        tree = None

    return tree


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    Takes in a FormulaTree rooted at root, returns the tree representation of
    the formula.
    REQ: root must be a valid FormulaTree
    >>> root1 = build_tree("(x+y)")
    >>> draw_formula_tree(root1)
    '+ y\\n  x'
    >>> root2 = build_tree("(-(x+y)*(x*y))")
    >>> draw_formula_tree(root2)
    '* * y\\n    x\\n  - + y\\n      x'
    '''
    # Base Case, root is a Leaf:
    # Draw the Leaf's symbol
    if isinstance(root, Leaf):
        tree = root.get_symbol()

    # Recursive Cases, root is any other FormulaTree
    # Call the helper function
    elif isinstance(root, FormulaTree):
        tree = formula_tree_helper(root, 0)

    return tree


def formula_tree_helper(root, branch):
    '''(FormulaTree, int) -> str
    Helper for draw_formula_tree.
    Takes in a FormulaTree rooted at root and the branch level of the root,
    returns the tree representation of the formula with specified indentation.
    REQ: root must be a valid FormulaTree
    REQ: branch >= 0
    >>> root1 = build_tree("(-(x+y)*(x*y))")
    >>> formula_tree_helper(root1, 0)
    '* * y\\n    x\\n  - + y\\n      x'
    '''
    # Base Case, root is a Leaf:
    # Draw the Leaf's symbol
    if isinstance(root, Leaf):
        tree = root.get_symbol()

    # Recursive Case, NotTree: Draw a '-', call the function on the NotTree's
    # child, create a new branch for the child
    elif isinstance(root, NotTree):
        tree = ('- ' + formula_tree_helper(root.get_children()[0], branch+1))

    # Recursive Case, AndTree/OrTree: Draw a '*' or '+'
    # Call the function on the AndTree/OrTree's children
    # Create a new branch for the children
    # Match up the second child's indentation with the first child
    elif isinstance(root, AndTree):
        child1 = root.get_children()[0]
        child2 = root.get_children()[1]
        tree = ('* ' + formula_tree_helper(child2, branch+1) + '\n  ' +
                ('  ' * branch) + formula_tree_helper(child1, branch+1))

    elif isinstance(root, OrTree):
        child1 = root.get_children()[0]
        child2 = root.get_children()[1]
        tree = ('+ ' + formula_tree_helper(child2, branch+1) + '\n  ' +
                ('  ' * branch) + formula_tree_helper(child1, branch+1))

    return tree


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    Takes in a FormulaTree rooted at root, a string of variables in the
    formula, and corresponding truth values (1s and 0s) for those variables.
    Returns the corresponding truth variable for the formula.
    REQ: root must be a valid FormulaTree
    REQ: variables must include all of the variables in root
    REQ: len(variables) == len(values)
    REQ: all variables must be unique
    REQ: values contains only '0' and '1'
    >>> evaluate(AndTree(Leaf('x'), Leaf('y')),'xy','11')
    1
    >>> evaluate(OrTree(AndTree(Leaf('y'), Leaf('z')), Leaf('x')),'xyz','001')
    0
    >>> evaluate(NotTree(Leaf('x')),'x','0')
    1
    '''
    # Assign each truth value in values to the corresponding
    # variable in variables
    formula_values = dict()
    for i in range(len(values)):
        formula_values[variables[i]] = int(values[i])

    # Base Case, root is a Leaf: the value is the value of the Leaf's symbol
    if isinstance(root, Leaf):
        value = formula_values[root.get_symbol()]

    # Recursive Cases, root is a tree

    # NotTree: value will be the opposite of the NotTree's child
    # Not(1) will be 0, Not(0), will be 1
    elif isinstance(root, NotTree):
        value = 1 - (evaluate(root.get_children()[0], variables, values))

    # AndTree: the value of both children must be equal to 1 for AndTree to
    # equal 1, else it will be 0
    # Thus, the value from AndTree is the minimum value of both children
    elif isinstance(root, AndTree):
        value = min(evaluate(root.get_children()[0], variables, values),
                    evaluate(root.get_children()[1], variables, values))

    # OrTree: the value of at least one child must be equal to 1 for OrTree to
    # equal 1, if both children are 0, then OrTree's value is 0
    # Thus, the value from OrTree is the maximum value of both children
    elif isinstance(root, OrTree):
        value = max(evaluate(root.get_children()[0], variables, values),
                    evaluate(root.get_children()[1], variables, values))

    return value


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int
    Takes in a FormulaTree rooted at root, a string representing the order
    of turns for Players A and E, a string of variables in the formula and
    corresponding truth variables (1s and 0s) for some of those variables.
    Returns the most optimal move to win the formula game (either a 1 or a 0
    depending on which player is playing).
    REQ: root must be a valid FormulaTree
    REQ: len(variables) == len(turns) > len(values)
    REQ: variables must include all of the variables in root
    REQ: all variables must be unique
    REQ: values contains only '0' and '1'
    >>> root1 = build_tree("((((x*y)+-z)*-w)+-(((a+b)*c)+d))")
    >>> play2win(root1, 'EAEAEAEA', 'wabcxdyz', '1000110')
    0
    >>> root2 = build_tree("((y*(-x+a))+(b*(-c*d)))")
    >>> play2win(root2, 'AEEAAE', 'ybxcad', '0')
    1
    '''
    # Set a variable for the winning value of the player who has their turn
    player_value = WIN_VALUE[turns[len(values)]]

    # Calculate the number of moves left; the number of winning combinations
    # will be 2^(moves_left)
    # Create a dictionary to record all the winning combinations when a
    # 0 is played, and also when a 1 is played
    moves_left = len(turns) - len(values)
    winning_moves = {'0': 0, '1': 0}

    # Each move combination can be represented as a string of 0s and 1s, or in
    # terms of a binary string
    for i in range(2 ** moves_left):

        # Calculate the binary form of each combination (i.e. bin(11) -> 1011)
        # Add zeroes to the beginning of the binary string for the final moves
        # to equal the number of moves left
        final_moves = bin(i)[2:].zfill(moves_left)

        # If the move combination returns a winning result, increment the
        # winning combinations of the move it starts with by 1
        if evaluate(root, variables, values + final_moves) == player_value:
            winning_moves[final_moves[0]] += 1

    # Choose the move that yields more winning possibilities
    print('1:', winning_moves['1'], ', 0:', winning_moves['0'])
    if winning_moves['1'] > winning_moves['0']:
        best_move = 1

    elif winning_moves['1'] < winning_moves['0']:
        best_move = 0

    # Else, pick the default
    else:
        best_move = player_value

    return best_move
