# Implementation of single and doubly linked list in this file

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

    # Add value after a certain node
    def addAfter(self,value,newValue):
        node = Node(newValue)
        head = self.head
        # Iterate till you reach the node
        while head != None:
            if (head.data == value):
                # If its the last node, add as it is
                if head.next == None:
                    head.next = node
                    node.prev = head
                    break
                # Else add prev to the node after the searched node
                else:
                    head.next.prev = node
                    node.next = head.next
                    head.next = node
                    node.prev = head
                    break
            head = head.next
    
    #Add value before a certain node
    def addBefore(self,value,newValue):
        node = Node(newValue)
        head = self.head
        # Iterate till you reach the node
        while head != None:
            if (head.data == value):
                # If its the head node, make this node the head node
                if head == self.head:
                    # this
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                    # or this
                    # addHead(self, newValue)
                    break
                # Else add value to the node before the searched node
                else:
                    head.prev.next = node
                    node.prev = head.prev
                    node.next = head
                    head.prev = node
                    break
            head = head.next

    def getLength(self):
        count = 0
        head = self.head
        while head != None:
            count += 1
            head = head.next
        return count

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

