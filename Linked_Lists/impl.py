# The basic Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
            node.prev = head
        # Else iterate till the end of the list and add the node
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current
    
    # Add an element to the top of the list
    def addHead(self,value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node

    # Print all the elements of the linked list
    def printAll(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next
    
    # Print all the elements in the linked list in reverse
    def printReverse(self):
        # Iterate to the last element
        current = self.head
        while current.next != None:
            current = current.next
        
        # Iterate back to the head element
        while current != None:
            print(current.data)
            current = current.prev

