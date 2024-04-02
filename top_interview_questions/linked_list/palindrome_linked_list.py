class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))


def is_palindrome(list):
    fast = slow = prev =list
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = None
    while fast.next != slow:





print(is_palindrome(list))
