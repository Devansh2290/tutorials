# Node class
class Node:
   # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveLoop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow = self.head
        fast = self.head
        # Move slow and fast 1 and 2 steps respectively
        slow = slow.next
        fast = fast.next.next
        # Search for loop using slow and fast pointers
        while (fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        # if loop exists
        print ("slow --- fast ---",slow.data, fast.data)
        if slow == fast:
            slow = self.head
            while (slow.next != fast.next):
                slow = slow.next
                fast = fast.next
            # Sinc fast.next is the looping point
            fast.next = None  # Remove loop

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data, end=' ')
            temp = temp.next
        print ('\n')


llist = LinkedList()
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
# Create a loop for testing
llist.head.next.next.next.next.next.next.next = llist.head.next.next
# print ("data --", llist.head.next.next.next.next.next.next.data)
# print ("data --", llist.head.next.next.data)
llist.detectAndRemoveLoop()
print ("Linked List after removing loop")
llist.printList()