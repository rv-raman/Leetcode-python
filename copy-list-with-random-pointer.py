"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if head==None:
        #     return None
        # dt_ll = {}
        # temp = head
        # while temp != None:
        #     dt_ll[temp]=Node(temp.val)
        #     temp=temp.next
        # temp = head
        # while temp!=None:
        #     cl = dt_ll[temp]
        #     if temp.next!=None:
        #         cl.next = dt_ll[temp.next]
        #     else:
        #         cl.next = None
        #     if temp.random!=None:
        #         cl.random = dt_ll[temp.random]
        #     else:
        #         cl.radom=None
        #     temp = temp.next
        # return dt_ll[head]
        itr= head
        front = head
        while itr!=None:
            front = itr.next
            c = Node(itr.val)
            itr.next = c
            c.next = front
            itr=front
        itr = head
        while itr!=None:
            if itr.random!=None:
                itr.next.random = itr.random.next
            if itr.next==None:
                break
            itr = itr.next.next
        dn = Node(0)
        ans=dn
        itr = head
        while itr!=None:
            if itr.next!=None:
                front = itr.next.next
            else:
                front = None
            dn.next = itr.next
            itr.next = front
            itr = front
            dn = dn.next
        return ans.next