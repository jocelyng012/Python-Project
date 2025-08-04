import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

    def test_enqueue_one_item(self):
        # enqueueing one item to an empty queue
        print("\n")
        q = lab1.Queue()
        q.enqueue(5)
        self.assertEqual(str(q), '[5]')
    
    def test_enqueue_and_dequeue_single_item(self):
        # testing enqueueing and dequeueing a single item
        print("\n")
        q = lab1.Queue()
        q.enqueue(10)
        self.assertEqual(q.dequeue(), 10)
        self.assertTrue(q.isEmpty())
    
    def test_dequeue_empty_queue(self):
        # dequeue() on an empty queue/stack should raise an exception
        print("\n")
        q = lab1.Queue()
        with self.assertRaises(AttributeError):
            q.dequeue()

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")
    
    def test_push_one_item(self):
        # pushing one item to an empty stack
        print("\n")
        s = lab1.Stack()
        s.push(5)
        self.assertEqual(str(s), '[5]')

    def test_dequeue_empty_queue(self):
        # pop() on an empty queue/stack should raise an exception
        print("\n")
        s = lab1.Stack()
        with self.assertRaises(AttributeError):
            s.pop()

    def test_push_and_pop_single_item(self):
        # testing pushing and popping a single item
        print("\n")
        s = lab1.Stack()
        s.push(10)
        self.assertEqual(s.pop(), 10)
        self.assertTrue(s.isEmpty())

class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_cap_and_spaces(self):
        # capital letters and spaces are valid inputs
        print("\n")
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")


if __name__ == '__main__':
    unittest.main()
