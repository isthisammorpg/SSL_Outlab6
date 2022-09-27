"""This module contains the implementation of abstract data type Heap.
"""
# --------------------------------- Heap --------------------------------

class Heap:
    """This class is the implementation of the abstract datatype Heap.

    This class has eight member functions of which one is the constructor:

    - __init__(cap) is the constructor
    - parent(i)
    - left(i)
    - right(i)
    - insert(val)
    - min()
    - Heapify(root)
    - deleteMin()

    :param H: This is the list whose elements are arranged in the form of a heap
    :type H: List
    :param n: This contains the number of elements in the heap
    :type n: int
    :param M: This contains the capacity of the heap
    :type M: int
    """
    def __init__(self, cap):
        """Constructor method for heap.
        |br| This initialises a list of size cap with all elements as None, sets the value of n to zero and value of M to cap.

        Example:
            >>> from Heap import *
            >>> sample = Heap(3)
            >>> print(sample.H)
            [None, None, None]
            >>> print(sample.n)
            0
            >>> print(sample.M)
            3
        """
        self.H = [None]*cap
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """This returns the index of the parent of the element(in the heap) at the given index.

        :param i: it is the index of the element whose parent's index is required to be returned
        :type i: int
        :return: Index of the parent of the element(in the heap) at the given index
        :rtype: int

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> print(sample.parent(1), sample.parent(2), sample.parent(3), sample.parent(4))
            0 0 1 1
        """
        return (i - 1) // 2
    
    def left(self, i):
        """This returns the index of the left of the element(in the heap) at the given index.
        
        :param i: it is the index of the element
        :type i: int
        :return: Index of the left of the element(in the heap) at the given index
        :rtype: int

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> print(sample.left(0), sample.left(1))
            1 3
        """
        return (2 * i) + 1
    
    def right(self, i):
        """This returns the index of the right of the element(in the heap) at the given index.
        
        :param i: it is the index of the element
        :type i: int
        :return: Index of the right of the element(in the heap) at the given index
        :rtype: int

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> print(sample.right(0), sample.right(1))
            2 4
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """Inserts the element with value(= val) in the heap.
        
        :param val: the value to be inserted
        :type val: int

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> print(sample.H)
            [1, 2, 4, 5, 3]
        """
        if self.n != self.M:
            self.H[self.n] = val
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """Returns the minimum element of the heap.
        
        :return: The minimum element of the heap
        :rtype: int

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> print(sample.min())
            1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """Establishes the basic properties of the heap in the heap.

        :param root: index of the root element of the heap to be heapified
        :type root: int
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """Deletes the minimum element of the heap and heapifies it.

        Example:
            >>> from Heap import *
            >>> sample = Heap(5)
            >>> sample.insert(5)
            >>> sample.insert(3)
            >>> sample.insert(4)
            >>> sample.insert(1)
            >>> sample.insert(2)
            >>> sample.deleteMin()
            >>> print(sample.H)
            [2, 3, 4, 5]
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.H.pop()
                self.Heapify(0)