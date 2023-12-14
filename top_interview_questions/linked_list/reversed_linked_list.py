class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


def reverse_list(head: [ListNode]) -> [ListNode]:
    current = head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


x = reverse_list(ll)
print(x)
