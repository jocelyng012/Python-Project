class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        new_node = Node(data) # follow the sildes, get the data
        if self.root is None: # check if tree is empty
            self.root = new_node # set it as a root
            return

        curr = self.root 
        while curr: # start traversing from the root
            if data < curr.data: # if data is smaller than curr, go to left
                if curr.left is None: # left node is empty
                    curr.left = new_node # insert
                    new_node.parent = curr # update the parent to curr
                    return # exit after inserting
                curr = curr.left # then move to left child of the curr
            else:
                if curr.right is None: # same as left side, right node is empty
                    curr.right = new_node # insert
                    new_node.parent = curr # update the parent
                    return # exit after inserting
                curr = curr.right # then move to right child of the curr


    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None: #if tree is empty
            return None 

        curr = self.root 
        while curr.left: # traverse the left subtree
            curr = curr.left # move to the left child
        return curr.data # return the leftmost data


    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None: #if tree is empty, same as min but right subtree
            return None 

        curr = self.root 
        while curr.right: # traverse the right subtree
            curr = curr.right # move to the right child
        return curr.data # return the rightmost data


    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        curr = self.root # start from the root
        while curr:
            if data == curr.data: # if match return
                return curr
            elif data < curr.data: # if the data smaller than curr, go to left child (left subtree)
                curr = curr.left
            else:
                curr = curr.right # if the data bigger than curr, go to right child (right subtree)
        return None # return none if not found


    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        return self.__find_node(data) is not None # use method above to check if we can found match node


    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type): # source: google
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        if curr_node is not None: # if the node is None
            if traversal_type == Tree.PREORDER: #preorder, root first
                yield curr_node.data
            yield from self.__traverse(curr_node.left, traversal_type) # traverse the left subtree

            if traversal_type == Tree.INORDER: #inorder, root after left subtree
                yield curr_node.data
            yield from self.__traverse(curr_node.right, traversal_type) #traverse the right subtree

            if traversal_type == Tree.POSTORDER: # postorder, root after both left and right
                yield curr_node.data


    def find_successor(self, data): #1. most left side of the right subtree
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        node = self.__find_node(data) # locate the node using __find_node.
        if not node: # if not exist in the tree
            raise KeyError(f"Node not exist")

        if node.right: # if node has right subtree
            curr = node.right # start from right child (subtree)
            while curr.left: # most left side of the right subtree
                curr = curr.left
            return curr
        
        curr = node # if not case 1, look at parent
        while curr.parent and curr == curr.parent.right: # traverse upward
            curr = curr.parent
        return curr.parent


    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        node_to_delete = self.__find_node(data)
        if node_to_delete is None:
            raise KeyError(f"Node not exist")
        
        # Case 1: no children
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent is None: # if the node is the root
                self.root = None 
            elif node_to_delete == node_to_delete.parent.left: # if the node is a left child
                node_to_delete.parent.left = None 
            else: # if the node is a right child
                node_to_delete.parent.right = None 
        
        # Case 2: 1 child
        elif node_to_delete.left is None:
            if node_to_delete.parent is None: # if the node is the root
                self.root = node_to_delete.right # child become root
                self.root.parent = None # clear child's parent (old root) pointer
            elif node_to_delete == node_to_delete.parent.left: # if the node is a left child
                node_to_delete.parent.left = node_to_delete.right # adopt the node's right child
                node_to_delete.right.parent = node_to_delete.parent 
            else: # if the node is a right child
                node_to_delete.parent.right = node_to_delete.right # adopt the node's right child
                node_to_delete.right.parent = node_to_delete.parent 

        elif node_to_delete.right is None:
            if node_to_delete.parent is None: # if the node is the root
                self.root = node_to_delete.left # child become root
                self.root.parent = None # clear child's parent (old root) pointer
            elif node_to_delete == node_to_delete.parent.left: # if the node is a left child
                node_to_delete.parent.left = node_to_delete.left # adopt the node's left child
                node_to_delete.left.parent = node_to_delete.parent 
            else: # if the node is a right child
                node_to_delete.parent.right = node_to_delete.left # adopt the node's left child
                node_to_delete.left.parent = node_to_delete.parent 
        
        # Case 3: 2 children
        else:
            successor = self.find_successor(node_to_delete.data)
            node_to_delete.data = successor.data # swap
            
            if successor.right: # if successor has right child
                if successor == successor.parent.left:
                    successor.parent.left = successor.right # replace successor with its right child
                else: # if successor has left child
                    successor.parent.right = successor.right # replace successor with its left child
                successor.right.parent = successor.parent # update parent pointer after swap
            else: # if successor has no children
                if successor == successor.parent.left:
                    successor.parent.left = None # remove successor from the left
                else:
                    successor.parent.right = None #remove successor from the left


t = Tree()
t.insert(7)
t.insert(5)
t.insert(9)
t.insert(3)
t.insert(6)
t.insert(8)
t.insert(10)
t.insert(1)
t.insert(2)

preorder = [node for node in t.preorder()]
inorder = [node for node in t.inorder()]
postorder = [node for node in t.postorder()]

print(preorder)
print(inorder)
print(postorder)