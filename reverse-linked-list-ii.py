# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None
        lt = []
        c = 0
        temp = head
        st = en = None
        while temp != None:
            c += 1
            if c == left - 1:
                st = temp
            if c >= left and c <= right:
                lt.append(temp)
            if c == right + 1:
                en = temp
            temp = temp.next
        if st == None:
            st = ListNode(-501)
            head = st
        while st != None and lt:
            st.next = lt.pop()
            st = st.next
        st.next = en
        if left == 1:
            return head.next
        else:
            return head


