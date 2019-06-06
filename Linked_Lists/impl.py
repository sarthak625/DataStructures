# The basic Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def addNext(next):
        self.next = next

# Implementation of a linked list
class LinkedList:
    # Initialize the linked list with a head node
    def __init__(self, data):
        self.head = Node(data)
    
    # Add elements to the end of the linked list
    def add(self,value):
        node = Node(value)
        head = self.head
        # If the head is None, make the new node the head node
        if head == None:
            head = node
        # If the linked list has just one node, add the node to the head's next
        elif head.next == None:
            head.next = node
        # Else iterate till the end of the list and add the node
        else:
            current = head
            while current != None:
                prev = current
                current = current.next
            prev.next = node
    
    # Print all the elements of the linked list
    def printAll(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next

