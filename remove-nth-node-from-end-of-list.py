# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        s = 0
        while temp != None:
            s += 1
            temp = temp.next
        req_pos = s - n + 1
        if req_pos == 1:
            head = head.next
            return head
        temp = head
        p = 0
        while temp != None:
            p += 1
            if p == req_pos - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head



