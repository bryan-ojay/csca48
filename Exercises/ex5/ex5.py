from week6_heap import Heap


def merge_heap(heap1, heap2):
    '''(Heap, Heap) -> Heap
    Takes in two min-heaps, returns a new heap with elements from both heaps
    inside.
    '''
    # Compare the size of the two heaps, the heap with the smaller size will
    # transfer all their objects to the bigger heap
    if (heap1.size() >= heap2.size()) or (heap2.is_empty()):
        heap_add = heap1
        heap_del = heap2

    elif (heap1.size() < heap2.size()) or (heap1.is_empty()):
        heap_add = heap2
        heap_del = heap1

    # While loop runs until the smaller heap has transferred all its elements
    while not heap_del.is_empty():
        # Remove the element from the smaller heap to the bigger heap
        heap_add.insert(heap_del.remove_last_node())

    return heap_add


def first_and_last(heap):
    '''(Heap) -> (obj, obj)
    Takes in a heap, returns the items with the highest and lowest priority
    REQ: heap.is_empty() == False
    '''
    # Extract the first item from the heap
    heap.upheap_bubbling()
    first_item = heap.min()
    last_item = first_item
    # Extract items from the heap in a loop until the last element is reached
    while not heap.is_empty():
        last_item = heap.extract_min()

    return (first_item, last_item)


if __name__ == "__main__":
    heap1 = Heap("Archer")
    names1 = sorted(["Bailey", "Baker", "Brewer", "Porter", "Potter",
                     "Sawyer", "Slater", "Smith", "Stringer", "Taylor",
                     "Butcher", "Carter", "Chandler", "Clark", "Collier"])
    for name in names1:
        heap1.insert(name)

    heap2 = Heap("Head")
    names2 = sorted(["Hunt", "Hunter", "Judge", "Knight", "Miller",
                     "Mason", "Page", "Palmer", "Parker", "Thatcher",
                     "Turner", "Walker", "Weaver"])
    for name in names2:
        heap2.insert(name)

    new_heap = merge_heap(heap1, heap2)

    names = ['Ye', 'Roy', 'Cai', 'Edwards', 'Alex', 'McMurray', 'Wong',
             'Zhang', 'Lam', 'Ran', 'Siu', 'Elliott', 'Thomas', 'Qin', 'Han',
             'Tam', 'Duong', 'Gallo', 'Ding', 'Ou', 'Hu', 'Yao', 'Xia',
             'Nathalia', 'Lyn', 'Ahmed', 'Jung', 'Shah', 'Fan', 'Do', 'Page',
             'Henderson', 'Xu', 'Tse', 'Muhammad', 'Joseph', 'Franco',
             'Samara', 'Bryan', 'Kang', 'Peng', 'Vance', 'Wan', 'Chan',
             'Bevers', 'Young', 'Lo', 'Ma', 'Ning']

    heap3 = Heap('Tu')
    for name in names:
        heap3.insert(name)

    heap3._heap = heap3._heap[::-1]

    print(first_and_last(heap3))
