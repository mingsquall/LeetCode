"""
Reverse a singly linked list.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
l_1 = ListNode(1)
l_2 = ListNode(2)
l_3 = ListNode(3)
l_1.next = l_2
l_2.next = l_3
l_3 = Solution().reverseList(l_1)

while l_3:
    print(l_3.val)
    l_3 = l_3.next

