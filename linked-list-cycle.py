# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''hashing approach'''
        # if head==None or head.next == None:
        #     return False
        # temp = head
        # s=set()
        # while temp!=None:
        #     if temp not in s:
        #         s.add(temp)
        #     else:
        #         break
        #     temp = temp.next
        # if temp!=None:
        #     return True
        # return False
        '''hare and tortoise approach'''
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

