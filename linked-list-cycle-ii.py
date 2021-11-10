# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        s = set()
        temp = head
        while temp != None:
            if temp not in s:
                s.add(temp)
            else:
                break
            temp = temp.next
        return temp

