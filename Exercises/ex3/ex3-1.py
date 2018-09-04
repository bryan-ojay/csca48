from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(up_dll, down_dll):
    '''(DoubleLinkedList, DoubleLinkedList) -> DoubleLinkedList
    Takes in a list sorted in ascending order and a list sorted
    in descending order. Returns a list with the elements of the two lists
    together, sorted in ascending order.
    >>> dll1, dll2 = DoubleLinkedList(), DoubleLinkedList()
    >>> dll1.add_last('A')
    >>> dll1.add_last('B')
    >>> dll1.add_last('C')
    >>> dll2.add_first('D')
    >>> dll2.add_first('E')
    >>> dll2.add_first('F')
    >>> str(reverse_merge(dll1, dll2))
    '(A, B, C, D, E, F)'
    '''
    # Create new double linked list
    new_dll = DoubleLinkedList()

    # create variables for the nodes in the ascending and descending lists
    # nodeA takes the first in the ascending list
    # nodeB takes the last in the descending list
    nodeA, nodeB = up_dll.get_first(), down_dll.get_last()

    # While loop checks if nodeA and nodeB are not None
    while (nodeA.get_element() is not None) or \
          (nodeB.get_element() is not None):

        # Check which element is smaller between the two
        # Insert the smaller element into the new_dll and remove it from the
        # original list to get the respected list's next smallest element
        if nodeA.get_element() is None:
            new_dll.add_last(nodeB.get_element())
            down_dll.remove_last()
            nodeB = down_dll.get_last()

        elif nodeB.get_element() is None:
            new_dll.add_last(nodeA.get_element())
            up_dll.remove_first()
            nodeA = up_dll.get_first()

        elif (nodeA.get_element() < nodeB.get_element()):
            new_dll.add_last(nodeA.get_element())
            up_dll.remove_first()
            nodeA = up_dll.get_first()

        elif (nodeA.get_element() > nodeB.get_element()):
            new_dll.add_last(nodeB.get_element())
            down_dll.remove_last()
            nodeB = down_dll.get_last()

        elif (nodeA.get_element() == nodeB.get_element()):
            new_dll.add_last(nodeA.get_element())
            up_dll.remove_first()
            down_dll.remove_last()
            nodeA = up_dll.get_first()
            nodeB = down_dll.get_last()

    return new_dll


def allocate_room(student_list, room, cap, index):
    '''(DoubleLinkedList, str, int, int) -> str
    Takes in a double linked list containing student's surnames, a string of
    a room name/number, an integer stating the capactiy of a room and an
    integer representing the index of the first student in the list. Returns a
    string showing the two first letters of the first and last person that
    should attend the room.
    REQ: cap > 0
    REQ: 0 < index < student_list.size()
    >>> dll1 = DoubleLinkedList()
    >>> dll1.add_last('AAA')
    >>> dll1.add_last('BBB')
    >>> dll1.add_last('CCC')
    >>> dll1.add_last('DDD')
    >>> dll1.add_last('EEE')
    >>> dll1.add_last('FFF')
    >>> allocate_room(dll1, 'ROOM101', 3, 1)
    'ROOM101 BB-DD'
    '''
    # We can't get the items without deleting items from the DLL
    # Get the first item from the student_list
    nodeA = student_list.get_first()

    # Make a for loop that runs through the list (range = index)
    #   Delete first item
    #   Get the new first item
    #   Keep going until you reach index, retrieve the element
    for i in range(index):
        student_list.remove_first()
        nodeA = student_list.get_first()

    name1 = nodeA.get_element()[:2]

    # Run a while loop that continues through the list (0 -> cap - 1)
    #   Delete first item
    #   Get the new first item
    #   Keep going until you reach the cap, retrieve element
    i = 0
    while i < cap - 1:
        last_name = student_list.remove_first()
        nodeA = student_list.get_first()
        if nodeA.get_element() is None:
            nodeA.set_element(last_name)
            i = cap - 1
        i += 1

    name2 = nodeA.get_element()[:2]

    return ("%s %s-%s" % (room, name1, name2))

if __name__ == "__main__":
    DLL_name1 = DoubleLinkedList()
    names1 = sorted(["Archer", "Bailey", "Baker", "Brewer", "Porter", "Potter",
                     "Sawyer", "Slater", "Smith", "Stringer", "Taylor",
                     "Butcher", "Carter", "Chandler", "Clark", "Collier"])
    for name in names1:
        DLL_name1.add_first(name) # Descending
        DLL_name2 = DoubleLinkedList()
        names2 = sorted(["Head", "Hunt", "Hunter", "Judge", "Knight", "Miller",
                         "Mason", "Page", "Palmer", "Parker", "Thatcher",
                         "Turner", "Walker", "Weaver"], reverse=True)
        for name in names2:
            DLL_name2.add_first(name) # Ascending

    dll_new = reverse_merge(DLL_name2, DLL_name1)
    print(dll_new)
    print(allocate_room(dll_new, "ROOM101", 3, 12))