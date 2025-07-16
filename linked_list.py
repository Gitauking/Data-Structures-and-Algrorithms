

#step one create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#step 2: create the nodes
node1 = Node('appple')
node2 = Node('banana')
node3 = Node('cherry')
node4 = Node('date')

#step three link them
node1.next = node2
node2.next = node3
node3.next = node4

head = node1 #keep reference to the first node


#traverse the linked list
current = node1
while current is not None:
    print(current.data)
    current = current.next

#counting fruits
count  = 0
current = head

while current is not None:
    count += 1
    current = current.next
print("Total fruits", count)

def remove_fruit(head, target):
    if head is None:
        return head

    # Case 1: If the head is the one to remove
    if head.data == target:
        return head.next
    
    # case 2: look for the target in the rest of the list
    current = head
    while current.next is not None:
        if current.next.data == target :
            current.next = current.next.next 
            break
        current = current.next

    return head

head = remove_fruit(head, "banana")

#print updated list
current = head
while current is not None:
    print(current.data)
    current = current.next