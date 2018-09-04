class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        '''(BTNode, int) -> NoneType
        Sets the depth of the given root node to the given depth, and all of
        its children to a depth 1 higher than its root.
        REQ: depth >= 0
        '''
        # Set the root depth to the given depth
        self.d = depth
        # Set the child's depth to the given depth + 1
        if self.left:
            self.left.set_depth(depth+1)
        if self.right:
            self.right.set_depth(depth+1)

    def leaves_and_internals(self):
        '''(BTNode) -> (set, set)
        Returns a set of all values stored in the leaves of the tree,
        and another set of all values stored in the internal nodes of the tree,
        rooted at this node.
        '''
        # Create leaves and internals for the root of the tree
        leaves, internals = (set(), set())

        # If a left subtree exists, add all of the leaves and internals of the
        # left subtree
        if self.left:
            left_values = self.left._leaf_int_helper()
            leaves = leaves.union(left_values[0])
            internals = internals.union(left_values[1])

        # If a right subtree exists, add all of the leaves and internals of the
        # right subtree
        if self.right:
            right_values = self.right._leaf_int_helper()
            leaves = leaves.union(right_values[0])
            internals = internals.union(right_values[1])

        elif not(self.left or self.right):
            leaves.add(self.value)

        return (leaves, internals)

    def _leaf_int_helper(self):
        '''(BTNode) -> (set, set)
        Returns a set of all values stored in the leaves of this subtree,
        and another set of all values stored in the internal nodes of this
        subtree, rooted at this node.
        '''
        # Create leaves and intervals for the root of the subtree
        leaves, internals = (set(), set())

        # Base Case: The subtree is a leaf if it has no children
        if not(self.left or self.right):
            leaves.add(self.value)

        # Recursive Cases
        # If the subtree has a left sub-subtree, the subtree is an internal
        if self.left:
            internals.add(self.value)
            left_values = self.left._leaf_int_helper()
            leaves = leaves.union(left_values[0])
            internals = internals.union(left_values[1])

        # If the subtree has a right sub-subtree, the subtree is an internal
        if self.right:
            internals.add(self.value)
            right_values = self.right._leaf_int_helper()
            leaves = leaves.union(right_values[0])
            internals = internals.union(right_values[1])

        return (leaves, internals)

    def sum_to_deepest(self):
        '''(BTNode) -> float
        Returns the sum of the longest path of nodes in the tree.
        '''
        # Get the sum from the helper
        return self._sum_helper(0)[1]

    def _sum_helper(self, depth):
        '''(BTNode) -> float
        Returns the sum of the longest path of nodes in the tree.
        REQ: depth >= 0
        '''
        # Set the total sum to be the node's value
        node_sum = self.value

        # Base Case, node is a leaf
        if not(self.left or self.right):
            node_depth, node_sum = (depth, self.value)

        # Recursive Cases
        # The subtree has a left and right child
        elif self.left and self.right:
            # Call the helper on both subtrees
            left_node = self.left._sum_helper(depth+1)
            right_node = self.right._sum_helper(depth+1)

            # Check whether the left subtree has a larger depth
            # or a larger/equal sum if the depths are the same
            if left_node >= right_node:
                node_depth = left_node[0]
                node_sum += left_node[1]

            # Check whether the right subtree has a larger depth
            # or a larger sum if the depths are the same
            elif left_node < right_node:
                node_depth = right_node[0]
                node_sum += right_node[1]

        # The subtree only has a left child: add the sum of the child to the
        # sum
        elif not self.right:
            left_node = self.left._sum_helper(depth+1)
            node_depth = left_node[0]
            node_sum += left_node[1]

        # The subtree only has a right child: add the sum of the child to the
        # sum
        elif not self.left:
            right_node = self.right._sum_helper(depth+1)
            node_depth = right_node[0]
            node_sum += right_node[1]

        return (node_depth, node_sum)


if (__name__ == "__main__"):
    # Just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
    # Tests on my_tree
    print(my_tree.set_depth(0))
    print(my_tree.leaves_and_internals())
    # returns ({5, 2, 9, 6}, {3, 4, 7})
    # where first index is leaves while second index is internals.
    print(my_tree.sum_to_deepest())
    # returns 30
    another_tree = BTNode(4, BTNode(2, BTNode(1), BTNode(5)),
                          BTNode(6, BTNode(10, BTNode(2)), BTNode(1)))
    print(another_tree)
    print(another_tree.leaves_and_internals())
    # Returns ({1, 2, 5}, {10, 2, 6})
    print(another_tree.sum_to_deepest())
    # returns 22
