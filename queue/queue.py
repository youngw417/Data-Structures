"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         if len(self) == 0:
#             self.storage.append(value)
#         else:
#             self.storage.insert(0, value)

#     def dequeue(self):
#         if len(self) == 0:
#             return None
#         return self.storage.pop()

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    


class Queue:
    def __init__(self):
        self.size = 0
        self.head = Node()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        newNode = Node(value)
        if len(self) == 0:
            self.head = newNode
            self.size = 1
        else:
            current = self.head
            for i in range(2, self.size + 1):
                current = current.next
            current.next = newNode
            self.size += 1

    def dequeue(self):
        if len(self) == 0:
            return None
        
        top = self.head
        self.head = self.head.next
        self.size -= 1
        return top.value