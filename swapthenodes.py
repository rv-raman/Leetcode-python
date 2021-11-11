class Node:
    def __init__(self, n):
        self.data = n
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertend(self, n):
        n = Node(n)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def print(self, curr=None):
        if curr == None:
            temp = self.head
        else:
            temp = curr
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def swapnodes(self, curr, i=0):
        if curr == None or curr.next == None:
            return curr

        if i % 2 != 0:
            curr.next = self.swapnodes(curr.next, i + 1)
            return curr

        else:
            h2 = self.swapnodes(curr.next, i + 1)
            temp = h2.next
            h2.next = curr
            curr.next = temp
            return h2


if __name__ == "__main__":
    n = int(input("enter number"))
    s = input("enter string of numbers")
    l = list(map(int, s.split(" ")))
    lobj = LinkedList()
    for i in l:
        lobj.insertend(i)
    lobj.print()
    k = lobj.swapnodes(lobj.head)
    lobj.print(k)

