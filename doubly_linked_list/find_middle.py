from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')
# return the middle node of the DLL if there are two nodes, return the left one
# no empty list, length >= 1
# 1 - 2 - 3 : 2
# 1 - 2 - 3 - 4 : 2
# 1 - 2 - 3 - 4 - 5 : 3


def find_middle(dll):
    # find length
    # floor divide
    h = dll.head
    t = dll.tail
    while h != t and h.next != t:
        h = h.next
        t = t.prev
    return h.value


# midtofind = DoublyLinkedList()
# midtofind.add_to_head(1)
# midtofind.add_to_head(2)
# midtofind.add_to_head(3)
# print(find_middle(midtofind))
# midtofind.add_to_head(4)
# print(find_middle(midtofind))
# midtofind.add_to_head(5)
# print(find_middle(midtofind))
# midtofind.add_to_head(6)
# midtofind.add_to_head(7)
# print(find_middle(midtofind))

odd_nums = DoublyLinkedList()
odd_nums.add_to_head(1)
odd_nums.add_to_head(2)
odd_nums.add_to_head(3)
odd_nums.add_to_head(4)
odd_nums.add_to_head(5)
odd_nums.add_to_head(6)
odd_nums.add_to_head(7)
print(find_middle(odd_nums))

even_nums = DoublyLinkedList()
even_nums.add_to_head(1)
even_nums.add_to_head(2)
even_nums.add_to_head(3)
even_nums.add_to_head(4)
even_nums.add_to_head(5)
even_nums.add_to_head(6)
even_nums.add_to_head(7)
even_nums.add_to_head(8)
even_nums.add_to_head(9)
even_nums.add_to_head(10)
print(find_middle(even_nums))

listofone = DoublyLinkedList()
listofone.add_to_head(1)
print(find_middle(listofone))

hugelist = DoublyLinkedList()
for i in range(1, 4000000):
    hugelist.add_to_tail(i)
print(find_middle(hugelist))
