"""This module contains the implementation of abstract data type Singly Linked List.
    |br| To achieve that, a Singly Linked List node (SinglyLinkedListNode) class has been implemented as well.
    |br| This module also contains a merge function useful for merging Singly linked lists.
"""
# ------------------------------- Singly Linked List -----------------------------


class SinglyLinkedListNode:
    """This is the class implementation of node for singly linked list.
    |br|  This node/object of this class has the property that it contains address of the next node in the list.

    This class has one constructor and one convertor:

    - __init__(data) is the constructor, and
    - __str__() is the convertor.
    """
    
    def __init__(self, data):
        """Constructor method for Singly linked list nodes. 
        |br| This sets the data to given data and next to none. 

        :param data: this is the value we want the node to contain
        :type data: any

        Example: 
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedListNode(10)
            >>> print(sample.data)
            10
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """Convertor method for Singly linked list nodes.
        |br| This returns the string form of the data stored in the node.

        :return: string form of data
        :rtype: str

        Example: 
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedListNode(10)
            >>> output = sample.__str__()
            >>> print(output)
            10
            >>> print(type(output))
            <class 'str'>
        """
        return str(self.data)

class SinglyLinkedList:
    """This is the class implementation of singly linked list.
        |br| The object of this class is a singly linked list of which address of only the head is known and each node has the address of the next node.
        
        This class has six member functions of which one is a constructor:

        - __init__() is the constructor
        - insert(data)
        - find(data)
        - deleteVal(data)
        - printer(sep)
        - reverse()
    """
    
    def __init__(self):
        """Constructor method for Singly Linked list.
        |br| This sets the the head and tail of the list to None.

        Example: 
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
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
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
            >>> sample.insert(10)
            >>> print(sample.head.data)
            10
            >>> print(sample.tail.data)
            10
            >>> sample.insert("11")
            >>> print(sample.head.data)
            10
            >>> print(sample.tail.data)
            11
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """Finds the node with the data stored in it and returns the node previous to/in front of it.

        :param data: It is the information we want to find in the linked list.
        :type data: any
        :return: previous node of the node which has the data.
        :rtype: SinglyLinkedListNode

        Example:
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> mynode = sample.find(22.5)
            >>> print(mynode.data)
            11
            >>> print(mynode.next.data)
            22.5
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev

    def deleteVal(self, data):
        """Deletes the node containing data if found.

        :param data: Data to be erased from the linked list.
        :type data: any
        :return: returns True if deleted successfully, else returns False if data not found in the list.
        :rtype: bool

        Example:
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> deleted = sample.deleteVal("11")
            >>> print(deleted)
            True
            >>> deletedTwice = sample.deleteVal("11")
            >>> print(deletedTwice)
            False
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next = prevPos.next.next
        return True
    
    def printer(self, sep = ', '):
        """Prints the linked list.

        :param sep: This tells us what should be used as a separator for distinct elements while printing the list, defaults to ', '
        :type sep: str, optional

        Example:
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
            >>> sample.insert(10)
            >>> sample.insert("11")
            >>> sample.insert(22.5)
            >>> sample.printer()
            [10, 11, 22.5]
            >>> sample.printer('-> ')
            [10-> 11-> 22.5]
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
            >>> from SinglyLinkedList import *
            >>> sample = SinglyLinkedList()
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
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """Merges two Singly Linked Lists into a single Singly Linked List.

    :param list1: Singly linked list 1
    :type list1: SinglyLinkedList
    :param list2: SinglyLinkedList 2
    :type list2: SinglyLinkedList
    :return: returns a singly linked list which is a combination of list1 and list2
    :rtype: SinglyLinkedList

    Example:
        >>> from SinglyLinkedList import *
        >>> sample1 = SinglyLinkedList()
        >>> sample2 = SinglyLinkedList()
        >>> sample1.insert(9)
        >>> sample1.insert(10)
        >>> sample1.insert(11)
        >>> sample2.insert(12)
        >>> sample2.insert(13)
        >>> sample2.insert(14)
        >>> sample = merge(sample1, sample2)
        >>> sample.printer()
        [9, 10, 11, 12, 13, 14]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged