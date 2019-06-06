# Implementation of circular linked list in this file

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
        self.head.next = self.head
        self.head.prev = self.head
    
    # Add elements to the end of the linked list
    def add(self,value):
        node = Node(value)
        head = self.head
        # If the head is None, make the new node the head node
        if head == None:
            head = node
            node.next = node
            node.prev = node
        # If the linked list has just one node, add the node to the head's next
        elif head.next == head:
            head.next = node
            head.prev = node
            node.prev = head
            node.next = head
        # Else iterate till the end of the list and add the node
        else:
            current = head
            while current.next != head:
                current = current.next
            current.next = node
            node.next = head
            node.prev = current
            head.prev = node
    
    # Add an element to the top of the list
    def addHead(self,value):
        node = Node(value)
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev = node
        self.head = node

    # Add value after a certain node
    def addAfter(self,value,newValue):
        node = Node(newValue)
        head = self.head
        changed = False
        # Iterate till you reach the node
        while head.next != self.head:
            if (head.data == value):
                head.next.prev = node
                node.next = head.next
                head.next = node
                node.prev = head
                changed=True
                break      
            head = head.next
        
        if (head.data == value and not changed):
            head.next = node
            node.prev = head
            node.next = self.head
            self.head.prev = node
    
    #Add value before a certain node
    def addBefore(self,value,newValue):
        node = Node(newValue)
        head = self.head
        changed = False
        # Iterate till you reach the node
        while head.next != self.head:
            if (head.data == value and head != self.head):   
                head.prev.next = node
                node.prev = head.prev
                node.next = head
                head.prev = node
                changed = True
                break
            if (head.data == value and head == self.head):
                # add a new head
                node.prev = self.head.prev
                node.next = self.head
                self.head = node
            head = head.next
        
        if (head.data == value and not changed):
            # If its the last node, add as it is
            node.prev = self.head.prev
            self.head.prev = node
            node.next = self.head
            self.head = node


    def getLength(self):
        count = 1
        head = self.head
        while head.next != self.head:
            count += 1
            head = head.next
        return count

    # Print all the elements of the linked list
    def printAll(self):
        head = self.head
        while head.next != self.head:
            print(head.data)
            head = head.next
        #print last element separately
        print(head.data)
    
    # Print all the elements in the linked list in reverse
    def printReverse(self):
        # Iterate to the last element
        current = self.head
        while current.next != self.head:
            current = current.next
        
        # Iterate back to the head element
        while current != self.head:
            print(current.data)
            current = current.prev
        print(current.data)

