def is_matched(exp):
    '''(str) -> bool
    Returns True if the brackets match
    >>> is_matched("(a+b)")
    True
    >>> is_matched("((a+b)")
    False
    >>> is_matched(")()(")
    False
    '''
    # Define a Stack
    exp_stack = Stack()
    
    for item in exp:
        if item == '(':
            exp_stack.push(item)
        elif item == ')':
            if (exp_stack.is_empty()):
                return False  #??????
            exp_stack.pop()
    return exp_stack.is_empty()

class EmptyStackError(Exception):
    '''An error to raise if an element is desired from an empty stack.'''
    
class Stack():
    '''A class to represent a stack'''
    
    def __init__(self):
        '''(Stack) -> NoneType
        Instantiates a new empty stack'''
        # Representation Invariant
        # _stack is a list
        # _stack[0] is the top of the stack
        # _stack[-1] is the bottom of the stack
        # _stack[:] shows the items in the stack
        self._stack = []
        
    def push(self, element):
        '''(Stack, obj) -> NoneType
        Inserts the given element at the top of the stack.
        '''
        self._stack.insert(0, element)
        
    def pop(self):
        '''(Stack) -> obj
        Removes and returns the element at the top of the stack.
        '''
        if self.is_empty():
            raise EmptyStackError("There are no elements in the stack.")
        element = self._stack.pop(0)
        return element
    
    def is_empty(self):
        '''(Stack) -> bool
        Returns True if there are no elements in the stack.
        '''
        return len(self._stack) == 0

    def top(self):
        '''(Queue) -> obj
        Returns the element at the beginning of the stack.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._stack[0]
        return element    
        
    def size(self):
        '''(Queue) -> int
        Returns the number of elements inside the queue.'''
        stack_size = len(self._stack)
        return stack_size
    
class Stack2():
    '''A class to represent a stack'''
    
    def __init__(self):
        '''(Stack) -> NoneType
        Instantiates a new empty stack'''
        # Representation Invariant
        # _stack is a dictionary
        # _stack[_front] is an int representing the top of the stack
        self._stack = {}
        self._front = 0
        
    def push(self, element):
        '''(Stack, obj) -> NoneType
        Inserts the given element at the top of the stack.
        '''
        self._stack[self._front] = element
        self._front += 1
        
    def pop(self):
        '''(Stack) -> obj
        Removes and returns the element at the top of the stack.
        '''
        if self.is_empty():
            raise EmptyStackError("There are no elements in the stack.")
        element = self._stack.pop(self._front - 1)
        self._front -= 1
        return element
    
    def is_empty(self):
        '''(Stack) -> bool
        Returns True if there are no elements in the stack.
        '''
        return len(self._stack) == 0

    def top(self):
        '''(Queue) -> obj
        Returns the element at the beginning of the stack.'''
        if self.is_empty():
            raise EmptyQueueError("There are no elements in the queue.")
        element = self._stack[self._front - 1]
        return element    
        
    def size(self):
        '''(Queue) -> int
        Returns the number of elements inside the queue.'''
        stack_size = len(self._stack)
        return stack_size
    
if __name__ == "__main__":
    stack1 = Stack()
    stack2 = Stack2()
    stack_list = [stack1, stack2]
    for s in stack_list:
        print('---')
        s.push(1)
        s.push(2)
        s.push(3)
        print(s._stack)
        print ("Queue Size 1:", s.size())
        print (s.is_empty())
        s.pop()
        s.pop()
        print(s._stack)
        print ("Queue Size 2:", s.size())
        print (s.top())
        s.pop()
        print(s.is_empty())