class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next



#TC

tc = ListNode(2)
tc.next = ListNode(1)
tc.next.next = ListNode(3)
tc.next.next.next = ListNode(4)

res = Solution.swapPairs(tc)
print (res)


# Ref : https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode

