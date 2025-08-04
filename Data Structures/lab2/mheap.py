class max_heap(object):
    """Binary max-heap 

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    A class for a binary max-heap data structure

    ...

    Attributes
    ----------
    heap: list
        A list of heap contents
    max_size: int
        The maximum capacity of the heap
    length: int
        The current position of elements in the heap

    Methods
    -------
    get_heap():
        Return the current heap as a list
    insert(data):
        Insert data into the heap and remain the max-heap property
    peek():
        Returns the maximum element in the heap without modify
    extract_max():
        Removes and returns the maximum element from the heap
    __heapify(curr_index, list_length = None):
        Ensures that the max-heap property is not violated
    build_heap():
        Build a max-heap from the current list of elements
    sort_in_place():
        Perform heatsort in-place and reorder elements in ascending order for self.heap
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations -- using __swap method.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap

    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        
        if self.length >= self.max_size:
            raise IndexError("Heap is Full")

        self.heap[self.length] = data # the last element is new data 
        curr = self.length # start heapsort from the last element

        while curr > 0: # if not reach to the head of the list 
            parent = self.__get_parent(curr) # get the parent node of the last element

            if self.heap[parent] < self.heap[curr]: #and curr bigger than the parent
                self.__swap(curr, parent) # swap the parent and curr
                curr = parent # curr now is the parent node
                # parent = self.__get_parent(curr) # parent now is the last parent's parent node\
            else:
                break

        self.length += 1 # increase the length

        
    def peek(self):
        """Return the maximum value in the heap."""
        if self.length == 0:
            raise KeyError("Heap is empty") # check if the heap is empty
        return self.heap[0] # the max value is the root, at index 0

    # def extract_max(self):
    #     """Remove and return the maximum value in the heap.

    #     Raises KeyError if the heap is empty."""
    #     # Tips: Maximum element is first element of the list
    #     #     : swap first element with the last element of the list.
    #     #     : Remove that last element from the list and return it.
    #     #     : call __heapify to fix the heap
    #     if self.length == 0:
    #         raise KeyError("Heap is empty")
        
    #     max_value = self.heap[0] # store the root
    #     self.heap[0] = self.heap[self.length - 1] # swap the root with the last, just index since the swap call the list
    #     self.length -= 1 # decrease the length
    #     self.__heapify(0, self.length) #start heapify at index 0 and down
    #     return max_value

    def __heapify(self, curr_index, list_length = None):
        """This function is ensures that the max-heap property is not violated, swap
        the value with its parent node is the value is greater than the parent node.
        Repeact the process until the max-heap property is satisfy for the whole tree.
        """
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        if list_length is None: 
            list_length = self.length

        # follow from the textbook
        largest = curr_index # assume the curr value is the largest
        left = self.__get_left(curr_index) # set the left node
        right = self.__get_right(curr_index) # set the right node

        if left < list_length and self.heap[left] > self.heap[largest]: # check if the left node is largest in the subtree
            largest = left # set the largest to the left node
        if right < list_length and self.heap[right] > self.heap[largest]: # check if the right node is largest in the subtree
            largest = right # set the largest to the right node

        if largest != curr_index: # if the largest of the subtree is not the curr index (curr node)
            self.__swap(curr_index, largest) # swap with the largest in record and curr index
            self.__heapify(largest, list_length) # recursive function

    def build_heap(self):
        """Convert the current list into a valid max-heap."""
        for i in range(self.length // 2 - 1, -1, -1):
            self.__heapify(i)

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == 0:
            raise KeyError("Heap is empty")
        
        max_value = self.heap[0] # store the root
        self.heap[0] = self.heap[self.length - 1] # swap the root with the last, just index since the swap call the list
        self.length -= 1 # decrease the length
        self.__heapify(0, self.length) #start heapify at index 0 and down
        return max_value

    def sort_in_place(self):
        """Perform heatsort in-place (e.g., reorder elements in ascending order for self.heap)
        Note that the heap is no longer "valid" once this method is called.
        Tip 1. Use the list_length parameter for __heapify method to limit the scope of self.heap
        Tip 2. Only use build_heap once, and then call __heapify for index where max-heap property is violated
        """
        self.build_heap()
        for i in range(self.length - 1, 0, -1): #start at last position to 0, step is -1)
            self.__swap(0, i) # swap the curr larger value to the end
            self.__heapify(0, i)

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    

def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    heap = max_heap(data=l)
    heap.sort_in_place()
    return l  # have to return, otherwise can't pass the test case: test_heap_sort_1



# test_list = [10, 3, 4, 7, 24, 57, 37, 67, 87]

# heap = max_heap(data=test_list)
# print("Heap after build_heap:", heap.get_heap())  

# heap.sort_in_place()
# print("Heap after sort_in_place:", heap.get_heap()) 
