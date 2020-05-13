from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
  

    def __len__(self):
        return self.size
  

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
      
    def pop(self):
        self.size -= 1
        return self.storage.remove_head()
      


mystack = Stack()
mystack.push(5)
mystack.push(10)
print(len(mystack))
print(mystack.pop())
print(len(mystack))
print(mystack.pop())
print(len(mystack))