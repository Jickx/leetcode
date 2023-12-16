class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(2, ListNode(3, ListNode(4)))


def merge(list1, list2):
    dummy = cur = ListNode
    while list1 and list2:
        if list1.value < list2.value:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        else:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
    if list1 or list2:
        cur.next = list1 if list1 else list2
    return dummy.next


result = merge(list1, list2)

while result:
    print(result.value)
    result = result.next
