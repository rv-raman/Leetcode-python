# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return False
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head = ListNode(0)
            temp = head
            c = 0
            while l1 != None and l2 != None:
                d = l1.val + l2.val + c
                if d > 9:
                    c = 1
                    d = d % 10
                else:
                    c = 0
                n = ListNode(d)
                temp.next = n
                temp = temp.next
                l1 = l1.next
                l2 = l2.next
            while l1 != None:
                d = l1.val + c
                if d > 9:
                    c = 1
                    d = d % 10
                else:
                    c = 0
                n = ListNode(d)
                temp.next = n
                temp = temp.next
                l1 = l1.next
            while l2 != None:
                d = l2.val + c
                if d > 9:
                    c = 1
                    d = d % 10
                else:
                    c = 0
                n = ListNode(d)
                temp.next = n
                temp = temp.next
                l2 = l2.next
            if c == 1:
                temp.next = ListNode(1)
        return head.next

