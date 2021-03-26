class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            node = Node(value, None)
            self.head = node
            node.next = node
        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            
            cur_node.next = Node(value, self.head)

    def print(self):
        result = ''
        cur_node = self.head
        while cur_node.next != self.head:
            result += str(cur_node.value) + ' '
            cur_node = cur_node.next
        result += str(cur_node.value)
        print(result)

linked = CircularLinkedList()

linked.append(1)
linked.append(3)
linked.print()
linked.append(5)
linked.append(7)
linked.print()
linked.append(9)
linked.append(11)
linked.print()