class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        for i in range(1, position):
            current = current.next
        if current == None:
            return None
        else:
            return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if position == 1: 
           new_element.next = self.head
           self.head = new_element
        else:
         for i in range(1, position - 1):
            current = current.next
         new_element.next = current.next
         current.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
           self.head = current.next
           current = None
           return
        else: 
           while current:
             if current.value == value:
              break
             prev = current
             current = current.next
           prev.next = current.next
           current = None
                
    def printList(self):
        current = self.head
        while current:
          print(current.value)
          current = current.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element("Test head")

# Setup LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.insert(e4, 4)
ll.delete(2)
ll.printList()
