class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """

    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object): #first in, first out
    """
    A class to represent a queue.

    ...

    Attributes
    ----------
    head : Node
        The first node in the queue
    tail : Node
        The last node in the queue
    Methods
    -------
    enqeue(newData):
        Adds a new node with the given data to the end of the queue
    deqeue():
        Removes and returns the data from the front of the queue
    isEmpty():
        Checks if the queue is empty
    """
    def __init__(self):
        self.__head = None #first node
        self.__tail = None #last node

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        curr = self.__head #set curr to first node
        result = []
        while curr:
            result.append(str(curr.getData())) #add node's data to list
            curr = curr.getNext() #after added, set curr to 
        return "[" + ", ".join(result) + "]" # join the result and return as string
 
    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        new_node = Node(newData) #create new node with new data
        if self.isEmpty():
            self.__head = self.__tail = new_node # if empty, all are the same data
        else:
            self.__tail.setNext(new_node) #curr tail's next node is the new node
            self.__tail = new_node #new data is the tail now

    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            raise AttributeError
        temp = self.__head # temp is the curr head
        self.__head = self.__head.getNext() #update the head to next node
        if self.__head is None: 
            self.__tail = None #if empty, none type
        return temp.getData() #return the temp data

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head is None #turn is head is none type


class Stack(object): #last in, first out
    """
    A class to represent a stack.

    ...

    Attributes
    ----------
    top : Node
        The top node in the stack

    Methods
    -------
    push(newData):
        Adds a new node with the given data to the top of the stack
    pop():
        Removes and returns the data from the top of the stack
    isEmpty():
        Checks if the stack is empty
    """
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        curr = self.__top #set curr to first node
        result = []
        while curr:
            result.append(str(curr.getData())) #add node's data to list
            curr = curr.getNext()
        return "[" + ", ".join(result) + "]" # join the result and return as string

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        new_node = Node(newData) #create new node with new data
        self.__top = new_node #new data is the top now

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            raise AttributeError
        temp = self.__top # temp is the curr head
        self.__top = self.__top.getNext() #update the head to next node
        return temp.getData() #return the temp data

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__top is None

def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value

    for char in s:
        myStack.push(char) #add data
        myQueue.enqueue(char) #add data

    while not myStack.isEmpty() and not myQueue.isEmpty(): #if both not empty
        if myStack.pop() != myQueue.dequeue(): #if they are not equal
            return False
    return True 

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return


result = isPalindrome("Eva Can I      Stab Bats In A Cave")
print(result)