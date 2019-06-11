# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
# Middle of linked list

import sys
sys.path.append('/home/sarthak/code/DataStructures/Linked_Lists')
from linkedlist import LinkedList

ll = LinkedList(12)
ll.add(27)
ll.add(29)
ll.add(39)
ll.add(49)
ll.add(59)
ll.add(69)
ll.add(40)

def middle(ll):
    head = ll.head
    mid = head

    while head != None:
        mid = mid.next
        head = head.next.next
    
    return mid

ll.printAll()
print("=============")
print middle(ll).data