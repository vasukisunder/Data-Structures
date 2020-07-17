"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node = self.head
            self.head = ListNode(value, None, node)
            node.prev = self.head
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None

        removedNode = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = removedNode.next
        self.length -= 1

        return removedNode
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None

        removedNode = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = removedNode.prev
        self.length -= 1

        return removedNode.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)


        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            if node == self.head:
                self.head = self.head.next
            if node == self.tail:
                self.tail = self.tail.prev
            
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        max_val = self.head.value
        current = self.head.next

        while current: 
            if current.value > max_val:
                max_val = current.value
            current = current.next

        return max_val