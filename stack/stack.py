"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)
#     def push(self, value):
#         self.storage.append(value)
#         self.size += self.size

#     def pop(self):
#         if len(self) == 0:
#             return None
#         else:
#             self.size -= self.size
#             return self.storage.pop()

class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(value):
        self.next = value




class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
  
    def is_empty(self):
        if self.head:
            return False
        else:
            return True


    def __len__(self):

        if self.is_empty():
            self.size = 0
        return self.size
            
        current = self.head
        count  = 1
        while current:
            count += 1
            curent = current.next
        self.size = count
        return self.size
  

    def push(self, value):
        newNode = Node(value)
      
        if not self.head:
            self.head = newNode
            self.size = 1
            
        
        else:
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def pop(self):

        if self.is_empty():
           return None
        top = self.head
        self.head = self.head.next
        self.size -= 1
        return top.value

      
        