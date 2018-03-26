#create a singly linked list

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append(self, new_element):
        """ add a new element at the end of a list """
        current = self.head
        if self.head:                   # if we have head element
            while current.next:         # loop until we have next element in a list
                current = current.next  # go through the list till the end
            current.next = new_element     # at the end of the list - place new element
        else:
            self.head = new_element     # if the list is empty, set new element to be the head

    
    def push(self, new_node):
        """add a new element at the beginning of a list """
        current = new_node
        current.next = self.head

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1                             # set counter to 1
        current = self.head                     # set start point of the list
        if position < 1:                        # if position was not set
            return None
        while current and counter <= position:  # looping through the list until position
            if counter == position:             # it required position is found
                return current                  # return the element
            current = current.next              # if not - continue looping
            counter += 1                        # increment counter each step
        return None                             # if position is not in a list


    def insert(self, new_element, position):
        """Insert a new node at the given position. Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:                        
            while current and counter < position:
                if counter == position - 1:             # find element after which we should add new
                    new_element.next = current.next     # set the link from new element to the next
                    current.next = new_element          # set the new element as a next to previous 
                current = current.next                  # looping through the list
                counter += 1                              
        elif position == 1:                             # insert new element at the very beginning of the list
            new_element.next = self.head                
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None                                  # set the previous element as None
        while current.value != value and current.next:   # looping till the end of the list until find a value
            previous = current                           # traversing through the list
            current = current.next
        if current.value == value:                       # if we find a value 
            if previous:                                 # having previous element
                previous.next = current.next             # change links from previous to the next skipping the current element in order to 'delete' it
            else:
                self.head = current.next                 # if we don't have previous element 

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value





