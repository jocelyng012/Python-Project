class Node(object):
    """
    A class for initialize node's left, right, parent, color
    """

    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """Red-Black Tree

    A red-black tree is a binary search tree with one extra bit of storage 
    per node: its color, which can be either RED or BLACK. By constraining 
    the node colors on any simple path from the root to a leaf, red-black 
    trees ensure that no such path is more than twice as long as any other, 
    so that the tree is approximately balanced.

    A class for a Red-Black Tree data structure.

    ...

    Attributes
    ----------
    root: Node
        The root node of the tree
    sentinel: Node
        A sentinel node used as NIL for all leaf nodes
    PREORDER: int
        For preorder traversal
    INORDER: int
        For inorder traversal
    POSTORDER: int
        For postorder traversal

    Methods
    -------
    print_tree():
        Print the data of all nodes in order
    print_with_colors():
        Prints the data of all node but with color indicators
    find_min():
        Travels across the leftChild of every node, and returns the node who has no leftChild
    find_node(data):
        Returns the Node object for the given data
    find_successor(data):
        Finds and returns the successor of the specified node
    insert(data):
        Adds a node to the tree
    bst_insert(self, data):
        Insertion for Binary Search Tree
    RB_transplant(u, v):
        Helper function for delection
    delete(data):
        Deletes a node with the specified key and rebalances the tree
    left_rotate(current_node):
        Performs a left rotation on the specified node
    right_rotate(current_node):
        Performs a right rotation on the specified node
    __rb_insert_fixup(z):
        Restores Red-Black Tree properties after an insertion
    __rb_delete_fixup(x):
        Restores Red-Black Tree properties after a deletion
    """

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color == "red": #fixed is to ==
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        current_node = self.root
        while current_node.left is not self.sentinel:
            current_node = current_node.left
        return current_node

    def find_min1(self, node=None):
        # added an new find_min that have optional parameters
        current_node = self.root if node is None else node
        while current_node.left is not self.sentinel:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node


    def RB_transplant(self, u, v):
        # helper function for delection from textbook 347
        if not u.parent: #if u.parent == self.sentinel:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def delete(self, data):
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        # from textbook 348
        node_to_delete = self.find_node(data)
        if node_to_delete is None:
            raise KeyError(f"Node not found")
        y = node_to_delete
        y_original_color = y.color

        if node_to_delete.left == self.sentinel:
            x = node_to_delete.right
            self.RB_transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.sentinel:
            x = node_to_delete.left
            self.RB_transplant(node_to_delete, node_to_delete.left)
        else:
            y = self.find_min1(node_to_delete.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.RB_transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self.RB_transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color
        
        # make sure the root is updated when the deleted node was the root
        if node_to_delete == self.root:
            self.root = y
        
        if y_original_color == "black":
            self.__rb_delete_fixup(x)
    

    def left_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x
        # refer page 328 of CLRS book for rotations
        # from the textbook P336
        if current_node.right == self.sentinel:
            raise KeyError(f"Left rotation does not exist")
        y = current_node.right
        current_node.right = y.left 
        if y.left != self.sentinel:
            y.left.parent = current_node
        y.parent = current_node.parent
        if current_node.parent == self.sentinel: # if curr node was the root
            self.root = y 
        elif current_node == current_node.parent.left: # if curr node was a left child
            current_node.parent.left = y
        else: # curr node was a right child, and now y is
            current_node.parent.right = y
        y.left = current_node
        current_node.parent = y
    

    def right_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y
        # refer page 328 of CLRS book for rotations
        # from the textbook P336
        if current_node.left == self.sentinel:
            raise KeyError(f"Right rotation does not exist")
        y = current_node.left
        current_node.left = y.right
        if y.right != self.sentinel:
            y.right.parent = current_node
        y.parent = current_node.parent
        if current_node.parent == self.sentinel: # if curr node was the root
            self.root = y 
        elif current_node == current_node.parent.right: # if curr node was a right child
            current_node.parent.right = y
        else: # curr node was a left child, and now y is
            current_node.parent.left = y
        y.right = current_node
        current_node.parent = y

    
    def __rb_insert_fixup(self, z):
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup
        # from the textbook P339
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                    # Case 1
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    # Case 2
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else: # if z's parent a right child
                y = z.parent.parent.left
                    # Case 1
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    # Case 2
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    # Case 3
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black" #  change root's color to black


    def __rb_delete_fixup(self, x):
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup
        # from the textbook P351
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                # Case 1
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                # Case 2
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                # Case 3
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else: # if x is a right child
                w = x.parent.left
                # Case 1
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                # Case 2
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                # Case 3
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black" # change x back to color black



# tree = rb_tree()
# tree.insert(7)
# tree.insert(5)
# tree.insert(9)
# tree.insert(3)
# tree.insert(6)
# tree.insert(8)
# tree.insert(10)
# tree.insert(1)
# tree.insert(2)

# tree.print_tree()
# print("intial prorder tree", "\n")

# tree.left_rotate(tree.root.right)
# tree_preorder = [node.data for node in tree.preorder()]
# tree.print_tree()
# print("tree after right rotation about root in prorder")