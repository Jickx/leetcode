class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


def reverse_list(head: [ListNode]) -> [ListNode]:
    current = head
    l = []
    while current:
        l.append(current.val)
        current = current.next

    def index(l):
        if not l:
            return None
        return ListNode(l.pop(), index(l))

    return index(l)


x = reverse_list(ll)
print(x)
