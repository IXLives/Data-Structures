from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# no recursion
# we cannot store the DLL and its data in other data structures


# def reverse(dll):
#     current = dll.head
#     new = current.next
#     current.next = None
#     old_tail = dll.tail
#     while new is not None:
#         prev = current
#         current = new
#         new = current.next
#         current.next = prev
#     return dll


def reverse(dll):
    temp = None
    current = dll.head

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    return dll


reverseme = DoublyLinkedList()
reverseme.add_to_tail(1)
reverseme.add_to_tail(2)
reverseme.add_to_tail(3)
reverseme.add_to_tail(4)
print(reverseme)
print(reverse(reverseme))
