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
        if self.value <= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
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

        if self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        if self.value == target:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # maximum value should be the rightmost value on the tree
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        if self.left:
            self.left.for_each(cb)

        cb(self.value)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node stack
        # push the current node onto stack
        # while we have items on stack
        # push left value of current node if we can
        # print current value and pop it off
        # push the right value of current node if we can
        node_stack = Stack()
        print(node.value)
        while node.left:
            print(node.left.value)
        while node.right:
            print(node.right.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print(bst)
