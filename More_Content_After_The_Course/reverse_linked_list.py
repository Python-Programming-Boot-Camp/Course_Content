class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None 
 
    def reverse(self, head):
        if head is None or head.next is None:
            return head
 
        rest = self.reverse(head.next)
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest
 
    # Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +str(temp.data) + " ")
            temp = temp.next
        return linkedListStr
 
    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
 
linkedList = LinkedList()
linkedList.add(20)
linkedList.add(4)
linkedList.add(15)
linkedList.add(85)
 
print("Original linked list" + str(linkedList))
 
linkedList.head = linkedList.reverse(linkedList.head)
 
print("Reversed linked list" + str(linkedList))