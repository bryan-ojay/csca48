class EmptyQueueError(Exception):
    '''An error to raise if an element is desired from an empty queue'''

class Queue():
    '''A class to represent a queue'''
    
    def __init__(self):
        '''(Queue) -> NoneType
        Instantiates a new empty queue'''
        # Representation Invariant
        # _queue is a list
        # _queue[0] represents the front/start of the queue
        # _queue[-1] represents the back/end of the queue
        # _queue[:] represents all the elements inside the queue
        self._queue = []
        
    def enqueue(self, element):
        '''(Queue, obj) -> NoneType
        Inserts the given element at the back of the queue.'''
        self._queue.append(element)
        
    def dequeue(self):
        '''(Queue) -> obj
        Removes and returns the element at the beginning of the queue.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._queue.pop(0)
        return element
    
    def is_empty(self):
        '''(Queue) -> bool
        Returns True there are no elements in the queue.'''
        return (len(self._queue) == 0)
        
    def front(self):
        '''(Queue) -> obj
        Returns the element at the beginning of the queue.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._queue[0]
        return element
    
    def size(self):
        '''(Queue) -> int
        Returns the number of elements inside the queue.'''
        queue_size = len(self._queue)
        return queue_size


class Queue2():
    '''A class to represent a queue'''
    
    def __init__(self):
        '''(Queue) -> NoneType
        Instantiates a new empty queue'''s
        # Representation Invariant
        # _queue is a dictionary (int:obj)
        # _first represents the front/start of the queue
        # _next represents the back/end of the list
        # _first and _next are integers
        # _next - _first = the number of elements in the queue
        # if _next > _first:
        #    _queue[first], _queue[first+1], ..., _queue[_next-1], _queue[next]
        #    are the elements in the order they were inserted
        self._queue = {}
        self._first = 0
        self._next = 0
        
    def enqueue(self, element):
        '''(Queue, obj) -> NoneType
        Inserts the given element at the back of the queue.'''
        # Insert the item at the "next" or following index
        # (i.e. if index 0 exists, the item is enqueued at index 1)
        self._queue[self._next] = element
        self._next += 1
        
    def dequeue(self):
        '''(Queue) -> obj
        Removes the element at the beginning of the queue.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._queue[self._first]
        self._queue.pop(self._first)  # Deletes the value at the first index
        # The first index is now deleted, change the first index to the next
        # index after it
        self._first += 1
        return element
    
    def is_empty(self):
        '''(Queue) -> bool
        Checks if there are no elements in the queue'''
        return (len(self._queue) == 0)
        
    def front(self):
        '''(Queue) -> obj
        Returns the element at the beginning of the queue.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._queue[self._first]
        return element
    
    def size(self):
        '''(Queue) -> int
        Returns the number of elements inside the queue.'''
        queue_size = len(self._queue)
        return queue_size

if __name__ == "__main__":
    queue1 = Queue()
    queue2 = Queue2()
    queue_list = [queue1, queue2]
    for q in queue_list:
        print('---')
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print ("Queue Size 1:", q.size())
        print (q.is_empty())
        q.dequeue()
        q.dequeue()
        print ("Queue Size 2:", q.size())
        print (q.front())
        q.dequeue()
        print(q.is_empty())