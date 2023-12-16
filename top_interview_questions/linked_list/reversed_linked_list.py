class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
ll = ListNode(1, ListNode(2, ListNode(3)))


def reverse_list(head):
    def reverse(head, prev=None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return reverse(n, head)

    return reverse(head, prev=None)


# def reverse_list(head):
#     if not head:
#         return None
#
#     new_head = head
#     if head.next:
#         new_head = reverse_list(head.next)
#         head.next.next = head
#     head.next = None
#
#     return new_head

# def reverse_list(head):
#     def reverse(cur, prev):
#         if cur is None:
#             return prev
#         else:
#             next = cur.next
#             cur.next = prev
#             return reverse(next, cur)
#
#     return reverse(head, None)


x = reverse_list(ll)
while x:
    print(x.val)
    x = x.next
