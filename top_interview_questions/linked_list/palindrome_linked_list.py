class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))


def is_palindrome(head) -> bool:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
    return True if result == result[::-1] else False


print(is_palindrome(list))
