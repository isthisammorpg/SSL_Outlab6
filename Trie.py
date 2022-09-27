"""This module contains the implementation of abstract data type Suffix Trie.
"""
# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """This is the class implementation of a Suffix Trie.
        |br| An instance of this class is a Trie which is used for the storage of various substrings of a string in the form of a tree with nodes where each node stores a character of the string.

        This class has five member functions one of which is a constructor:

        - __init__() is the constructor
        - find(root, c)
        - insert(s)
        - checkPrefix(s)
        - countPrefix(s)
    """
    
    def __init__(self):
        """Constructor method for Suffix Trie.
        |br| This sets the class variable T to an empty dictionary.

        Example:
            >>> from Trie import *
            >>> sample = Trie()
            >>> print(sample.T)
            {}
            >>> print(type(sample.T))
            <class 'dict'>
        """
        self.T = {}
    
    def find(self, root, c):
        """Finds the element c(character) in the heap and returns its position?.

        :param root: It is the dictionary in which character c is to be searched
        :type root: dict
        :param c: Character to be searched in the dictionary
        :type c: char
        :return: returns True if found, else returns False
        :rtype: bool

        Example:
            >>> from Trie import *
            >>> sample = Trie()
            >>> sample.insert('sample')
            >>> print(sample.find(sample.T, 's'))
            True
        """
        return (c in root)
    
    def insert(self, s):
        """Inserts a given string into the Trie.

        :param s: string to be inserted
        :type s: str

        Example:
            >>> from Trie import *
            >>> sample = Trie()
            >>> sample.insert('Tree')
            >>> print(sample.find(sample.T, 'T'), sample.find(sample.T['T'], 'r'), sample.find(sample.T['T']['r'], 'e'), sample.find(sample.T['T']['r']['e'], 'e'))
            True True True True
            >>> print(sample.T)
            {'T': {'#': 1, 'r': {'#': 1, 'e': {'#': 1, 'e': {'#': 1}}}}}
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """Checks if the given string s is present as prefix in the suffix trie.

        :param s: string to be checked
        :type s: str
        :return: True if found, else return False
        :rtype: bool

        Example:
            >>> from Trie import *
            >>> sample = Trie()
            >>> sample.insert('Stunning')
            >>> print(sample.checkPrefix('Stun'))
            True
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """Counts the number of prefixes of the string s in the Suffix Trie.

        :param s: The string whose prefix count is required
        :type s: str
        :return: prefix count of s
        :rtype: int

        Example:
            >>> from Trie import *
            >>> sample = Trie()
            >>> sample.insert('Vaibhav')
            >>> sample.insert('Vaibhavi')
            >>> sample.insert('Vaishnavi')
            >>> sample.insert('Vishal')
            >>> sample.insert('Raman')
            >>> print(sample.countPrefix('V'), sample.countPrefix('Vai'), sample.countPrefix('Vaibhav'))
            4 3 2
            >>> print(sample.countPrefix('R'), sample.countPrefix('Tarzan'))
            1 0
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0