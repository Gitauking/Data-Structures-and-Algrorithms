class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)#add to the top

    def pop(self):
        if not self.is_empty():
            return self.items.pop()#removes the first item at the top
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]#look at the top
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

stack = Stack()
stack.push('book')
stack.push('notebook')
stack.push('pen')
stack.push('scissors')
stack.push('sharpener')

print('top of the stack:', stack.peek())#pen

stack.pop() #removes pen
print('new top after popping', stack.peek())

print('stack size:', stack.size())