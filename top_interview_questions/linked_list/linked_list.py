class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, new_element):
        current = self.head
        while True:
            if current.next:
                current = current.next
            else:
                current.next = new_element
                break

    def print_ll(self):
        current = self.head
        result = []
        while True:
            if current:
                result.append(current.value)
                current = current.next
            else:
                break
        print(result)

    def delete_by_value(self, value):
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

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def delete_by_index(self, index):
        current = self.head
        for _ in range(self.__len__() - index):
            previous = current
            current = current.next
        if current == self.head:
            self.head = current.next
        else:
            previous.next = current.next


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


ll.print_ll()
ll.delete_by_index(1)
ll.print_ll()
