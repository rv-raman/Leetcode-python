# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, lhead):
        t1 = lhead
        prev = None
        while t1 != None:
            t = t1.next
            t1.next = prev
            prev = t1
            t1 = t
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = self.reverseList(l1)
        ll2 = self.reverseList(l2)
        c = 0
        dummy = ListNode(0)
        temp = dummy
        while ll1 != None or ll2 != None or c != 0:
            sum = 0
            if ll1 != None:
                sum += (ll1.val)
                ll1 = ll1.next
            if ll2 != None:
                sum += (ll2.val)
                ll2 = ll2.next
            if c != 0:
                sum += c

            c = sum // 10
            sum = sum % 10
            n = ListNode(sum)
            temp.next = n
            temp = n
        return self.reverseList(dummy.next)



