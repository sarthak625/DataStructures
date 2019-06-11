# https://www.geeksforgeeks.org/flattening-a-linked-list/
# Flattening a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def addRight(self, value):
        # If there is no element after head

        head = self.head

        while head.right != None:
            head = head.right
            
        head.right = Node(value)
    
    def addDown(self, at, value):
        head = self.head

        while head != None:
            if head.value == at:
                current = head

                while current.down != None:
                    current = current.down
                
                current.down = Node(value)
                break
            head = head.right

    def printAll(self):
        head = self.head

        matrix = []

        while head != None:
            down = []
            current = head

            if current.down != None:
                current = current.down
                while current!=None:
                    down.append(current.value)
                    current = current.down

            matrix.append([head.value, down])
            head = head.right

        print matrix 

ll = LinkedList(8)

ll.addRight(10)
ll.addDown(10,11)
ll.addDown(10,12)
ll.addDown(10,13)
ll.addDown(10,14)
ll.addDown(10,15)
ll.addRight(20)
ll.addDown(20,21)
ll.addDown(20,22)
ll.addDown(20,23)
ll.addDown(20,24)
ll.addRight(30)
ll.addDown(30,34)
ll.addDown(30,35)
ll.addRight(40)
ll.addRight(50)
ll.addDown(50,51)

def flatten(ll):
    head = ll.head

    newList = None

    while head != None:
        if newList == None:
            newList = LinkedList(head.value)
        else:
            newList.right = Node(head.value)
            newList = newList.right
        
        current = head
        while current != None:
            newList.right = Node(head.value)
            current = current.down

        head = head.right
    
    return newList

def printFlattenedList(head):
    while head!=None:
        print(head.value)
        head = head.right

newList = flatten(ll)

printFlattenedList(newList)
