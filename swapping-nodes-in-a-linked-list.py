# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        t1 = t2 = t3 = head
        c = 0
        while t1 != None:
            c += 1
            if c == k:
                break
            t1 = t1.next
        t3 = t1
        while t3.next != None:
            t2 = t2.next
            t3 = t3.next
        t = t1.val
        t1.val = t2.val
        t2.val = t
        return head

#         if head == None:
#             return None
#         temp = head
#         s=0
#         while temp!=None:
#             s+=1
#             temp = temp.next
#         temp = head
#         p=0
#         while temp!=None:
#             p+=1
#             if k==p:
#                 d1 = temp.val
#             if (s-k+1)==p:
#                 d2 = temp.val

#             temp= temp.next
#         temp = head
#         p=0
#         while temp!=None:
#             p+=1
#             if k==p:
#                 temp.val = d2
#             if (s-k+1)==p:
#                 temp.val=d1
#             temp= temp.next
#         return head


