import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

class T6_insert(unittest.TestCase):

    def test_insert1(self):
        print("\n")
        print("Insert test")
        t = lab3.Tree()

        t.insert(12)
        t.insert(10)
        t.insert(11)
        t.insert(5)
        t.insert(8)
        t.insert(7)
        t.insert(9)
        t.insert(3)
        t.insert(4)
        t.insert(1)
        t.insert(17)
        t.insert(13)
        t.insert(15)
        t.insert(20)
        t.insert(18)
        t.insert(23)

        self.assertEqual(t.root.data, 12)
        self.assertEqual(t.root.left.data, 10)
        self.assertEqual(t.root.left.left.data, 5)
        self.assertEqual(t.root.left.right.data, 11)
        self.assertEqual(t.root.right.data, 17)
        self.assertEqual(t.root.right.left.data, 13)
        self.assertEqual(t.root.right.right.data, 20)


        print("\n")

class T7_traversal(unittest.TestCase):

    def test_traversal1(self):
        print("\n")
        print("Traversals test")
        t = lab3.Tree()

        t.insert(12)
        t.insert(10)
        t.insert(11)
        t.insert(5)
        t.insert(8)
        t.insert(7)
        t.insert(9)
        t.insert(3)
        t.insert(4)
        t.insert(1)
        t.insert(17)
        t.insert(13)
        t.insert(15)
        t.insert(20)
        t.insert(18)
        t.insert(23)

        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]
        
        print("inorder traversal")
        self.assertEqual(inorder, [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 23])
        print("preorder traversal")
        self.assertEqual(preorder, [12, 10, 5, 3, 1, 4, 8, 7, 9, 11, 17, 13, 15, 20, 18, 23])
        print("postorder traversal")
        self.assertEqual(postorder, [1, 4, 3, 7, 9, 8, 5, 11, 10, 15, 13, 18, 23, 20, 17, 12])

        print("\n")

class T8_find_node(unittest.TestCase):

    def test_find_node(self):
        print("\n")
        print("Find-node test")
        t = lab3.Tree()

        t.insert(12)
        t.insert(10)
        t.insert(11)
        t.insert(5)
        t.insert(8)
        t.insert(7)
        t.insert(9)
        t.insert(3)
        t.insert(4)
        t.insert(1)
        t.insert(17)
        t.insert(13)
        t.insert(15)
        t.insert(20)
        t.insert(18)
        t.insert(23)

        self.assertEqual(t._Tree__find_node(10).data, 10)
        self.assertEqual(t._Tree__find_node(1).data, 1)
        self.assertEqual(t._Tree__find_node(23).data, 23)
        self.assertIsNone(t._Tree__find_node(24))
        self.assertIsNone(t._Tree__find_node(0))
        self.assertIsNone(t._Tree__find_node(50))
        
        print("\n")

class T9_contains(unittest.TestCase):

    def test_contains1(self):
        print("\n")
        print("Contains test")
        t = lab3.Tree()

        t.insert(12)
        t.insert(10)
        t.insert(11)
        t.insert(5)
        t.insert(8)
        t.insert(7)
        t.insert(9)
        t.insert(3)
        t.insert(4)
        t.insert(1)
        t.insert(17)
        t.insert(13)
        t.insert(15)
        t.insert(20)
        t.insert(18)
        t.insert(23)

        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), True)
        self.assertEqual(t.contains(40), False)
        self.assertEqual(t.contains(24), False)

        print("\n")

class T10_successor(unittest.TestCase):

    def test_successor1(self):
        print("\n")
        print("Successor test")
        tree_success = lab3.Tree()

        tree_success.insert(12)
        tree_success.insert(10)
        tree_success.insert(11)
        tree_success.insert(5)
        tree_success.insert(8)
        tree_success.insert(7)
        tree_success.insert(9)
        tree_success.insert(3)
        tree_success.insert(4)
        tree_success.insert(1)
        tree_success.insert(17)
        tree_success.insert(13)
        tree_success.insert(15)
        tree_success.insert(20)
        tree_success.insert(18)
        tree_success.insert(23) 

        easy_success = tree_success.find_successor(5).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(15).data

        self.assertEqual(easy_success, 7)
        self.assertEqual(medium_success, 11)
        self.assertEqual(tough_success, 17)

        print("\n")

class T11_delete(unittest.TestCase):

    def test_delete1(self):
        print("\n")
        print("Delete test")
        t = lab3.Tree()

        t.insert(12)
        t.insert(10)
        t.insert(11)
        t.insert(5)
        t.insert(8)
        t.insert(7)
        t.insert(9)
        t.insert(3)
        t.insert(4)
        t.insert(1)
        t.insert(17)
        t.insert(13)
        t.insert(15)
        t.insert(20)
        t.insert(18)
        t.insert(23)

        l1 = [node for node in t]
        t.delete(1)
        l2 = [node for node in t]
        t.delete(13)
        l3 = [node for node in t]
        t.delete(11)
        l4 = [node for node in t]
        t.delete(20)

        self.assertEqual(l1, [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 23]) #inorder
        self.assertEqual(l2, [3, 4, 5, 7, 8, 9, 10, 11, 12, 15, 17, 18, 20, 23])
        self.assertEqual(l3, [3, 4, 5, 7, 8, 9, 10, 12, 15, 17, 18, 20, 23])
        self.assertEqual(l4, [3, 4, 5, 7, 8, 9, 10, 12, 15, 17, 18, 23])

        print("\n")

class T11_delete(unittest.TestCase):

    def test_delete_empty(self):
        print("\n")
        print("Delete empty test")
        t = lab3.Tree()

        with self.assertRaises(KeyError):
            t.delete(7)
        
        print("\n")

class T12_successor(unittest.TestCase):

    def test_successor_empty(self):
        print("\n")
        print("Successor empty test")
        tree_success = lab3.Tree()

        with self.assertRaises(KeyError):
            success = tree_success.find_successor(8).data
        
        print("\n")


if __name__ == '__main__' :
    unittest.main()