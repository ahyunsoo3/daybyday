class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry: # check if l1 or l2 is value of 0. If they have a value of 0, which affects the result that is not calculable.
        v1 = v2 = 0
        if l1: # as above mentioned, ListNode is defined as 0 or 1 if they are or not.
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10) # quotient and remainder
        n.next = ListNode(val)
        n = n.next
    return root.next # the root connected c.


# Ref : https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward