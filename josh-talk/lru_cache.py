class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def insertOnHead(self, key, value):
        # create node with the given value
        node = Node(key, value)
        node.next = self.head

        # in case if list is not empty
        if self.head:
            self.head.prev = node

        self.head = node

        # in case list was empty
        if not self.end:
            self.end = node
        return node

    def removeNode(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev

    def printList(self):
        if not self.head:
            return
        curr_node = self.head

        while curr_node:
            print(f'{curr_node.key}: {curr_node.value}', end=" | ")
            curr_node = curr_node.next

        print('\n')


class LRUCache:
    def __init__(self, size=3):
        self.size = size
        self.dlist = DoubleLinkedList()
        self.hash_map = {}

    # O(1)
    def get(self, key):
        # key alreadt exist in hash_map
        if key in self.hash_map:
            # 1. get the node from hash_map
            node = self.hash_map[key]

            # 2. remove the node from its current position
            self.dlist.removeNode(node)

            # 3. insert it agine on head of list
            self.dlist.insertOnHead(node.key, node.value)
            print(f"{key} accessed from cache.")

            return node.value
        print(f'{key} not in cache')
        return -1

    # O(1)
    def put(self, key, value):
        # key already exists in hash_map
        if key in self.hash_map:

            # 1. get the node from hash_map
            node = self.hash_map[key]

            # 2. remove the node from its current position
            self.dlist.removeNode(node)

            # 3. insert it agine on head of list
            self.dlist.insertOnHead(key, value)
        else:
            if len(self.hash_map) >= self.size:
                # 1. remove the key from hash_map which is end of dlist
                self.hash_map.pop(self.dlist.end.key)

                # 1. remove the end node from dlist
                self.dlist.removeNode(self.dlist.end)

            node = self.dlist.insertOnHead(key, value)
            self.hash_map[key] = node


objLRU = LRUCache()
objLRU.dlist.printList()

objLRU.put(1, 5)
objLRU.dlist.printList()

objLRU.put(2, 7)
objLRU.dlist.printList()

objLRU.put(3, 8)
objLRU.dlist.printList()

objLRU.get(1)
objLRU.dlist.printList()

objLRU.put(3, 9)
objLRU.dlist.printList()

objLRU.put(5, 15)
objLRU.dlist.printList()