"""This module contains the implementation of abstract data type Doubly Linked List.
    |br| To achieve that, a Doubly Linked List node (DoublyLinkedListNode) class has been implemented as well.
"""
# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """This is the class implementation of node for doubly linked list.
        |br| This node/object of this class has the property that it contains address of the next as well as the previous node in the list.

        This class has one constructor and one convertor:

        - __init__(data) is the constructor, and
        - __str__() is the convertor.
    """
    
    def __init__(self, data):
        """Constructor method for node of Doubly linked list.
        |br| This sets the data of the of the node to given data and next and prev to None.

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedListNode(10)
            >>> print(sample.data)
            10
            >>> print(sample.next)
            None
            >>> print(sample.prev)
            None
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """Convertor method for Doubly Linked list node.
        |br| Returns the string form of data stored at the node.

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedListNode(10)
            >>> output = sample.__str__()
            >>> print(output)
            10
            >>> print(type(output))
            <class 'str'>
        """
        return str(self.data) 

class DoublyLinkedList:
    """This is the class implementation of doubly linked list. 
        |br| The objects of this class are doubly linked lists of whom the address of both the head and the tail are known and, 
        each node has the address of both the next and previous nodes.

        This class has four member functions of which one is a constructor:

        - __init__() is the constructor
        - insert(data)
        - printer(sep)
        - reverse() 
    """
    
    def __init__(self):
        """Constructor method for doubly linked list.
        |br| This sets the head and tail of the list to None.

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedList()
            >>> print(sample.head)
            None
            >>> print(sample.tail)
            None
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """Inserts a new node which contains given data behind the tail of the list.

        :param data: It is the information to be stored in the linked list.
        :type data: any

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> print(sample.head.data, sample.head.next.data, sample.head.prev)
            10 11 None
            >>> print(sample.tail.data, sample.tail.next, sample.tail.prev.data)
            22.5 None 11
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """Prints the linked list.

        :param sep: This tells us what should be used as a separator for distinct elements while printing the list, defaults to ', '
        :type sep: str, optional

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> sample.printer()
            [10, 11, 22.5]
            >>> sample.printer('<-> ')
            [10<-> 11<-> 22.5]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """Reverses the linked list.

        Example:
            >>> from DoublyLinkedList import *
            >>> sample = DoublyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> sample.printer()
            [10, 11, 22.5]
            >>> sample.reverse()
            >>> sample.printer()
            [22.5, 11, 10]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev