class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            current.next = new_element

    def print_linked_list(self):
        current = self.head
        result = []
        while True:
            if current:
                result.append(current.value)
                current = current.next
            else:
                break
        return result

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    break
                else:
                    previous.next = current.next
                    break
            else:
                previous = current
                current = current.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

ll = LinkedList(node1)

ll.append(node2)
ll.append(node3)
ll.append(node4)
ll.append(node5)

ll.delete(2)

print(ll.print_linked_list())
