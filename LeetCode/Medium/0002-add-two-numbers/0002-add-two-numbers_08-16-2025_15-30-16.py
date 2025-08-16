from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def listnode_to_rev_number(l1 :Optional[ListNode]):
    n1 = 0
    count = 0
    while l1:
        n1 = n1 + l1.val * (10 ** count)
        l1 = l1.next
        count += 1
    return n1

def num_to_rev_listnode(num: int):
    num = str(num)[::-1]
    listres = ListNode()
    current_listres = listres
    for i in num:
        current_listres.next = ListNode(int(i))
        # print(current_listres.val)
        current_listres = current_listres.next
    return listres.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #construct l1 reversed
        n1 = listnode_to_rev_number(l1)
        # print(n1)
        n2 = listnode_to_rev_number(l2)
        # print(n2)
        res = n1 + n2
        # print(res)
        res_listnode = num_to_rev_listnode(res)
        return res_listnode
