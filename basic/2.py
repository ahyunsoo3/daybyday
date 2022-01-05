# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Find materials.
# => Even, there are times when you have to find data elsewhere that are not provided here. Of course, the compensation for doing so is certain.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1, l2):
    carry = 0;
    res = n = ListNode(0); # what's different res and n? are they sharing variance in a reference way?
    while l1 or l2 or carry: # "carry" needed for what?
        if l1:
            carry += l1.val
            l1 = l1.next;
        if l2:
            carry += l2.val;
            l2 = l2.next;
        carry, val = divmod(carry, 10) # after executing this, stored carry seem to be useless.
        n.next = n = ListNode(val);
    return res.next;


# list = ListNode(2)
# print(list.val)
# print(list.next)
#
# list.next = ListNode(3)
# print("\n\n- added ListNode(3) -")
# print(list.next)
# print(list.next.val)
# print(list.next.next)
#
#
# list.next.next = ListNode(4)
# print("\n\n- added ListNode(4) -")
# print(list.next.next.val)
# print(list.next.next.next)
#
# print("\n\n- Sum of index 0, 1 in ListNode -")
# result = list.val + list.next.val
# print(result)



