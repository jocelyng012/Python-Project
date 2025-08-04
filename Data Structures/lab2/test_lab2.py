import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):

    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

class T6_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(4)
        pq.insert(3)
        pq.insert(6)
        self.assertEqual(pq.peek(), 6)
        print("\n")

class T7_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [0,6,8,4,5,2,78,10]
        sorted_list = mheap.heap_sort(to_sort_list)
        self.assertEqual(sorted_list, [0, 2, 4, 5, 6, 8, 10, 78])
        print("\n")

class T8_heap_build(unittest.TestCase):

    def test_heap_build_correctness(self):
        initial_data = [15, 5, 20, 1, 17, 10, 30, 8, 25]
        heap = mheap.max_heap(data=initial_data)
        heap.build_heap() 
        expected_heap = [30, 25, 20, 8, 17, 10, 15, 5, 1]
        self.assertEqual(heap.get_heap(), expected_heap)
        print("\n")


class T9_heap_insert(unittest.TestCase):
    def test_1_heap_insert(self):
        heap = mheap.max_heap(size = 3)
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        with self.assertRaises(IndexError):
            heap.insert(4)
        print("\n")

class T10_heap_extract_max(unittest.TestCase):

    def test_1_extract_max_empty(self):
        heap = mheap.max_heap(size = 5)
        with self.assertRaises(KeyError):
            heap.extract_max()
        print("\n")

class T11_pqueue_validity(unittest.TestCase):

    def test_1_pq_insert_extract_validity(self):
        pq = pqueue.pqueue(10)
        pq.insert(5)
        pq.insert(9)
        pq.insert(2)
        pq.insert(7)
        pq.extract_max()
        pq.insert(8)
        pq.extract_max()
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [7, 5, 2])
        print("\n")
    
if __name__ == '__main__':
    unittest.main()