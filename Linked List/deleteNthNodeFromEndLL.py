# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ahead = head
        behind = head
        count = 1
        while ahead.next:
            if count > n:
                behind = behind.next
            count+= 1
            ahead = ahead.next
        # print(behind.val,ahead.val,"count",count,"n",n)
        if count == n:
            head = head.next
        else:
            behind.next = behind.next.next
        return head