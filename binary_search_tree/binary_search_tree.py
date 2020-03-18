from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # BinarySearchTree
        self.right = None  # BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to current node
        # if smaller go left
        # if greater go right
        # if no node to go to (left or right)
        # make new node at that spot
        curNode = self.value
        if curNode > value:
            if self.right is None:
                self.right = value
            else:
                curNode = self.right
        if curNode < value:
            if self.left is None:
                self.left = value
            else:
                curNode = self.left
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        # compare value to current node value
        # if smaller, go left
        # if larger, go right
        # if equal return true
        # if smaller but no left
        # return false
        # if larger but no right
        # return false
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
