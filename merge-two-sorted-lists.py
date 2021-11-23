# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        ans = l1
        while l1 != None and l2 != None:
            while l1 != None and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            temp.next = l2
            l1, l2 = l2, l1
        return ans

#         head = ListNode()
#         temp = head
#         while l1!=None and l2!=None:
#             if l1.val<=l2.val:
#                 head.next = l1
#                 l1=l1.next
#                 head = head.next
#             else:
#                 head.next = l2
#                 l2 = l2.next
#                 head = head.next
#         while l1!=None:
#             head.next = l1
#             l1=l1.next
#             head = head.next
#         while l2!=None:
#             head.next = l2
#             l2=l2.next
#             head = head.next
#         return temp.next
