"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head and not self.head:
            print('No node to remove')
         
            return None
        
        if self.head == self.tail:
            popped = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return popped

        removed = self.head
        self.head  = self.head.next
        self.length -= 1
        return removed.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not self.head and not self.head:
            self.add_to_head(value)
        else:
            new_node = ListNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def print_list(self):
        if not self.head and not self.head:
            print('No node to print')
        
        current = self.head
        while current:
            print(current.value)
            current = current.next
         
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head and not self.head:
            print('No node to remove')
            return None
        if self.head == self.tail:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        removed = self.tail
        self.tail.prev.next = None
        self.tail = removed.prev
        self.length -= 1
        return removed.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if not self.head and not self.head:
            print('No node to move')
            return None

        
        node.prev.next = node.next
        node.next = self.head
        self.head.prev = node
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if not self.head and not self.head:
            print('No node to move')
            return None
        if node == self.head:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            self.add_to_tail(value)
            return None
        if node == self.tail:
            return None

        node.prev.next = node.next
        # node = self.tail.next
        # node.prev = self.tail
        # self.tail = node
        self.length -= 1
        self.add_to_tail(node.value)
       

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.head:
            print('No node to delete')
            return None
        if  self.length == 1:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        
        if node == self.head:
       
            return self.remove_from_head()

        if node == self.tail:
            return self.remove_from_tail()

        removed = node.value
        node.prev.next = node.next
        self.length -= 1
        return removed

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head and not self.head:
            return None

        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next
            
        return max

# ddl = DoublyLinkedList()
# ddl.add_to_head(100)
# ddl.add_to_head(200)
# ddl.add_to_head(300)
# ddl.add_to_tail(400)
# ddl.add_to_tail(500)

# ddl.print_list()
# ddl.remove_from_tail()
# print('\n')
# ddl.print_list()
# ddl.move_to_front()
