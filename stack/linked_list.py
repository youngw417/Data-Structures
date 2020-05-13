class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    # def get_next(self):
    #     return self.next

    # def set_next(value):
    #     self.next = value

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head and not self.tail:
            return True
        else:
            return False

    def contains(self, value):
        if self.is_empty():
            return False
        
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
            
        return False

    def get_max(self):
        if self.is_empty():
            return None

        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next
            
        return max


    def add_to_head(self, value):
        newNode = Node(value)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def add_to_tail(self, value):
        newNode = Node(value)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove_head(self):
        
        if self.is_empty():
            return None
        print('myhead', self.head)
        value = self.head.value
    
        self.head = self.head.next
        return value

    # def remove_from_tail(self):
    #     if is_empty():
    #         return None
        
    def print_ll_elements(self):
        if self.is_empty():
            print('no value in this linked list')
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next

# ll = LinkedList()
# ll.add_to_head(5)
# ll.add_to_head(7)
# print(ll.remove_head())
# print(ll.remove_head())