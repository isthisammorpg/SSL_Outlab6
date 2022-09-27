"""This module contains the implementation of abstract data type Binary Search Tree.
    |br| To achieve that, a Binary Search Tree node (BSTNode) class has been implemented as well.
"""
# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """This is the class implementation of node for binary search tree.
        |br| This node/object of this class has the property that it contains address of the left and right child of itself.

        This class has one constructor and one convertor:
        
        - __init__(data) is the constructor, and
        - __str__() is the convertor.
    """
    
    def __init__(self, info):
        """Constructor method for node of Binary Search Tree.
        |br| This stores the given value(info) in info and sets the left, right and level to None.

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BSTNode(10)
            >>> print(sample.info)
            10
            >>> print(sample.left)
            None
            >>> print(sample.right)
            None
            >>> print(sample.level)
            None
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """Convertor method for node of binary search tree.
        |br| This returns the string form of the info stored in the node.

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BSTNode(10)
            >>> output = sample.__str__()
            >>> print(output)
            10
            >>> print(type(output))
            <class 'str'>
        """
        return str(self.info)

class BinarySearchTree:
    """This is the class implementation of Binary Search Tree.
       |br| An instance of this class represents a Binary Search Tree which supports insertion at a node, traversal of tree and finding height of a node.

        This class has four member functions of which one is a constructor:

        - __init__() is the constructor
        - insert(val)
        - traverse(order)
        - height(root)
    """
    
    def __init__(self):
        """Constructor method for BST.
        |br| This sets the root to None.

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BinarySearchTree()
            >>> print(sample.root)
            None
        """
        self.root = None
    
    def insert(self, val):
        """Inserts a BST node with info as the value(val) given in the Binary Search Tree.

        :param val: Data to be stored in the BST, must be of type considering comparison operator
        :type val: any

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BinarySearchTree()
            >>> sample.insert(10)
            >>> sample.insert(9)
            >>> sample.insert(22.5)
            >>> print(sample.root.info, sample.root.left.info, sample.root.right.info)
            10 9 22.5
            >>> print(sample.root.left.left, sample.root.left.right, sample.root.right.left, sample.root.right.right)
            None None None None
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """This prints the tree depending upon the traversal we want.

        :param order: This is the type of traversal we want for the tree
        :type order: str

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BinarySearchTree()
            >>> sample.insert(4)
            >>> sample.insert(2)
            >>> sample.insert(3)
            >>> sample.insert(1)
            >>> sample.insert(6)
            >>> sample.insert(5)
            >>> sample.insert(7)
            >>> sample.traverse('PRE') # doctest: +NORMALIZE_WHITESPACE
            4 2 1 3 6 5 7
            >>> sample.traverse('IN')  # doctest: +NORMALIZE_WHITESPACE
            1 2 3 4 5 6 7
            >>> sample.traverse('POST')  # doctest: +NORMALIZE_WHITESPACE
            1 3 2 5 7 6 4
        """
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """This function gives the height of the tree traversing the tree from the root till the farthest leaf.

        :param root: denotes the starting node
        :type root: BSTNode
        :return: returns the distance of the node given from its farthest leaf
        :rtype: int

        Example:
            >>> from BinarySearchTree import *
            >>> sample = BinarySearchTree()
            >>> sample.insert(4)
            >>> sample.insert(2)
            >>> sample.insert(3)
            >>> sample.insert(1)
            >>> sample.insert(6)
            >>> sample.insert(5)
            >>> sample.insert(7)
            >>> print(sample.height(sample.root))
            2
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))