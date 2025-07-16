class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)#add to the back

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)#remove from the front
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]#see front
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

queue = Queue()

queue.enqueue("Alice")
queue.enqueue("Brian")
queue.enqueue("Donald")
queue.enqueue("Kevin")
queue.enqueue("Elvis")
queue.enqueue("Dan")
queue.enqueue("Charlene")
queue.enqueue("Alva")
queue.enqueue("Sharon")

print("First in line:", queue.peek())

print("queue size:", queue.size())

